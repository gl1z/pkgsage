# PkgSage

PkgSage analyses .NET build errors and suggests the NuGet package most likely to fix them.

Instead of searching for what `CS0246: The type or namespace name 'JsonConvert' could not be found` actually means, run PkgSage and get the answer directly.

## How it works

PkgSage runs `dotnet build` on your project, parses the compiler output for missing type errors (`CS0246`, `CS0234`, `CS0103`, `CS0012`), looks them up in a local SQLite database of symbol-to-package mappings, and prints the most likely `dotnet add package` command with a confidence score.

Each suggestion is verified against the live NuGet API — if the package doesn't exist on nuget.org the confidence drops. Results are cached locally so repeated runs don't hit the network.

## Installation

```bash
pip install -e .
```

## Usage

```bash
pkgsage path/to/MyProject.csproj
```

If you pass a `.csproj` directly, PkgSage will also filter out packages you've already referenced — no duplicate suggestions.

Example output:

```
Running dotnet build on MyProject.csproj...
[CS0246] Could not find 'JsonConvert'
→ dotnet add package Newtonsoft.Json  (confidence: 0.95)
[CS0246] Could not find 'ServiceCollection'
→ dotnet add package Microsoft.Extensions.DependencyInjection  (confidence: 0.95)
```
Output flags:

```bash
pkgsage path/to/MyProject.csproj --json           # structured JSON output
pkgsage path/to/MyProject.csproj --github-summary # Markdown table for GitHub Actions step summaries
```

## Current coverage

Around 70 symbols across common NuGet packages — Newtonsoft.Json, Entity Framework Core, AutoMapper, FluentValidation, MediatR, Dapper, Serilog, Polly, RestSharp, Microsoft.Extensions.*, Hangfire, Refit, AutoFixture, xUnit, NUnit, Moq, and more.

## Roadmap

- [x] CS0012 assembly-to-package resolution
- [x] Filter suggestions against already-referenced packages in `.csproj`
- [x] Confidence scoring with live NuGet verification
- [x] JSON and GitHub Actions summary output
- [ ] Solution-level support (`pkgsage MyApp.sln`)
- [ ] `--apply` mode to auto-install high-confidence suggestions
- [ ] `--dry-run` mode to generate a `.ps1`/`.sh` install script
- [ ] Live NuGet symbol index to replace manual seed data

## Contributing

The symbol database lives in `data/seed.sql`. If a package is missing, adding it is a one line SQL insert. Contributions welcome.