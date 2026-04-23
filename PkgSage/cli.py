import argparse
from PkgSage.runner import run_build
from PkgSage.parser import parse_errors
from PkgSage.resolver import resolve

def main():
    parser = argparse.ArgumentParser(
        description="PkgSage — suggests NuGet packages for .NET build errors"
    )
    parser.add_argument("project", help="path to .csproj file or project directory")
    parser.add_argument("--csproj", help="path to .csproj for installed package filtering", default=None)
    args = parser.parse_args()

    print(f"Running dotnet build on {args.project}...")
    returncode, output = run_build(args.project)

    if returncode == 0:
        print("Build succeeded, nothing to fix.")
        return

    errors = parse_errors(output)

    if not errors:
        print("Build failed but no recognisable missing type errors found.")
        print(output)
        return

    suggestions = resolve(errors, csproj_path=args.csproj)

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