import xml.etree.ElementTree as ET
from PkgSage.db import init_db, lookup
from PkgSage.nuget import check_package


def get_installed_packages(csproj_path):
    try:
        tree = ET.parse(csproj_path)
        root = tree.getroot()
        return {
            ref.get("Include").lower()
            for ref in root.iter("PackageReference")
            if ref.get("Include")
        }
    except Exception:
        return set()


def _split_cs0012_type(full_type):
    base = full_type.split("`")[0]
    parts = base.rsplit(".", 1)
    if len(parts) == 2:
        return parts[1], parts[0]
    return base, None


def _score(row, nuget_result):
    score = 0.50

    if row["namespace"]:
        score += 0.20

    if row["confidence"] >= 9:
        score += 0.10

    if nuget_result:
        if nuget_result.get("found"):
            score += 0.10
        if nuget_result.get("latest_version"):
            score += 0.05

    return round(min(score, 1.0), 2)


def resolve(errors, csproj_path=None):
    init_db()
    installed = get_installed_packages(csproj_path) if csproj_path else set()
    suggestions = []

    for error in errors:
        symbol = error["symbol"]
        namespace = error["namespace"]

        if error["code"] == "CS0012":
            symbol, namespace = _split_cs0012_type(symbol)

        rows = lookup(symbol, namespace)
        rows = [r for r in rows if r["package"].lower() not in installed]

        if not rows:
            suggestions.append({
                "code": error["code"],
                "symbol": error["symbol"],
                "package": None,
                "confidence": 0.0,
            })
            continue

        best = rows[0]
        nuget = check_package(best["package"])
        confidence = _score(best, nuget)

        suggestions.append({
            "code": error["code"],
            "symbol": error["symbol"],
            "package": best["package"],
            "confidence": confidence,
        })

    return suggestions