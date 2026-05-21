import argparse
import json
from PkgSage.runner import run_build
from PkgSage.parser import parse_errors
from PkgSage.resolver import resolve

def main():
    parser = argparse.ArgumentParser(
        description="PkgSage — suggests NuGet packages for .NET build errors"
    )
    parser.add_argument("project", help="path to .csproj file or project directory")
    parser.add_argument("--csproj", help="path to .csproj for installed package filtering", default=None)
    parser.add_argument("--json", action="store_true", help="output results as JSON")
    args = parser.parse_args()

    csproj_path = args.csproj
    if csproj_path is None and args.project.endswith(".csproj"):
        csproj_path = args.project

    print(f"Running dotnet build on {args.project}...", flush=True) if not args.json else None

    returncode, output = run_build(args.project)

    if returncode == 0:
        if args.json:
            print(json.dumps({"status": "ok", "suggestions": []}))
        else:
            print("Build succeeded, nothing to fix.")
        return

    errors = parse_errors(output)

    if not errors:
        if args.json:
            print(json.dumps({"status": "no_matches", "suggestions": []}))
        else:
            print("Build failed but no recognisable missing type errors found.")
            print(output)
        return

    suggestions = resolve(errors, csproj_path=csproj_path)

    if args.json:
        print(json.dumps({"status": "ok", "suggestions": suggestions}))
        return

    print()
    for s in suggestions:
        if s["package"]:
            print(f"[{s['code']}] Could not find '{s['symbol']}'")
            print(f"  → dotnet add package {s['package']}")
        else:
            print(f"[{s['code']}] Could not find '{s['symbol']}' — no match in database")
        print()

if __name__ == "__main__":
    main()