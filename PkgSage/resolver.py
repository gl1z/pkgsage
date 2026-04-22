from PkgSage.db import init_db, lookup, get_connection

def get_installed_packages(csproj_path: str) -> set[str]:
    import xml.etree.ElementTree as ET
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

def resolve(errors: list[dict], csproj_path: str | None = None) -> list[dict]:
    init_db()
    installed = get_installed_packages(csproj_path) if csproj_path else set()
    suggestions = []

    for error in errors:
        rows = lookup(error["symbol"], error["namespace"])
        rows = [r for r in rows if r["package"].lower() not in installed]

        if not rows:
            suggestions.append({
                "code": error["code"],
                "symbol": error["symbol"],
                "package": None,
            })
            continue

        # take the highest confidence match
        best = rows[0]
        suggestions.append({
            "code": error["code"],
            "symbol": error["symbol"],
            "package": best["package"],
        })

    return suggestions