import urllib.request
import json
from PkgSage.db import get_cached_nuget, set_cached_nuget

def check_package(package):
    cached = get_cached_nuget(package)
    if cached is not None:
        return cached

    url = f"https://api.nuget.org/v3-flatcontainer/{package.lower()}/index.json"
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            data = json.loads(resp.read())
            versions = data.get("versions", [])
            latest = versions[-1] if versions else None
            result = {"found": True, "latest_version": latest}
    except urllib.error.HTTPError:
        result = {"found": False, "latest_version": None}
    except Exception:
        return None

    set_cached_nuget(package, result["found"], result["latest_version"])
    return result