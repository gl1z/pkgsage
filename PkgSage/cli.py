import argparse
import json
from PkgSage.runner import run_build
from PkgSage.parser import parse_errors
from PkgSage.resolver import resolve


def render_github_summary(suggestions):
    lines = ["## PkgSage — Missing Package References", ""]

    matched = [s for s in suggestions if s["package"]]
    unmatched = [s for s in suggestions if not s["package"]]

    if matched:
        lines += [
            "| Error | Symbol | Package | Confidence |",
            "|-------|--------|---------|------------|",
        ]
        for s in matched:
            lines.append(f"| `{s['code']}` | `{s['symbol']}` | `{s['package']}` | {s['confidence']} |")

        lines += ["", "### Fix commands", "```"]
        for s in matched:
            lines.append(f"dotnet add package {s['package']}")
        lines.append("```")

    if unmatched:
        lines += ["", "### No match found", ""]
        for s in unmatched:
            lines.append(f"- `{s['code']}` `{s['symbol']}` — not in database")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="PkgSage — suggests NuGet packages for .NET build errors"
    )
    parser.add_argument("project", help="path to .csproj file or project directory")
    parser.add_argument("--csproj", help="path to .csproj for installed package filtering", default=None)
    parser.add_argument("--json", action="store_true", help="output results as JSON")
    parser.add_argument("--github-summary", action="store_true", help="output Markdown for GitHub Actions step summary")
    args = parser.parse_args()

    csproj_path = args.csproj
    if csproj_path is None and args.project.endswith(".csproj"):
        csproj_path = args.project

    silent = args.json or args.github_summary
    if not silent:
        print(f"Running dotnet build on {args.project}...")

    returncode, output = run_build(args.project)

    if returncode == 0:
        if args.json:
            print(json.dumps({"status": "ok", "suggestions": []}))
        elif args.github_summary:
            print("## PkgSage\n\nBuild succeeded, no missing packages.")
        else:
            print("Build succeeded, nothing to fix.")
        return

    errors = parse_errors(output)

    if not errors:
        if args.json:
            print(json.dumps({"status": "no_matches", "suggestions": []}))
        elif args.github_summary:
            print("## PkgSage\n\nBuild failed but no recognisable missing type errors found.")
        else:
            print("Build failed but no recognisable missing type errors found.")
            print(output)
        return

    suggestions = resolve(errors, csproj_path=csproj_path)

    if args.json:
        print(json.dumps({"status": "ok", "suggestions": suggestions}))
    elif args.github_summary:
        print(render_github_summary(suggestions))
    else:
        print()
        for s in suggestions:
            if s["package"]:
                print(f"[{s['code']}] Could not find '{s['symbol']}'")
                print(f"  → dotnet add package {s['package']}  (confidence: {s['confidence']})")
            else:
                print(f"[{s['code']}] Could not find '{s['symbol']}' — no match in database")
            print()


if __name__ == "__main__":
    main()