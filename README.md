# PkgSage

PkgSage analyses .NET build errors and suggests the NuGet package most likely to fix them.

Instead of searching for what `CS0246: The type or namespace name 'JsonConvert' could not be found` actually means, run PkgSage and get the answer directly.

## How it works

PkgSage runs `dotnet build` on your project, parses the compiler output for missing type errors (`CS0246`, `CS0234`, `CS0012`), looks them up in a local SQLite database of symbol-to-package mappings, and prints the most likely `dotnet add package` command.

## Installation

```bash
pip install platformdirs
pip install -e .
```

## Usage

```bash
pkgsage path/to/MyProject.csproj
```
Example output:

```
Running dotnet build on MyProject.csproj...

[CS0246] Could not find 'JsonConvert'
  → dotnet add package Newtonsoft.Json

[CS0246] Could not find 'IMapper'
  → dotnet add package AutoMapper
```

## Current coverage

The database currently covers ~30 common NuGet packages including Newtonsoft.Json, Entity Framework Core, AutoMapper, FluentValidation, MediatR, Dapper, Serilog, Polly, RestSharp, and more.

## Roadmap

- [ ] Expand symbol database
- [ ] Pull live mappings from the NuGet symbol index
- [ ] Support `CS0012` assembly-to-package resolution
- [ ] Filter suggestions against already-referenced packages in `.csproj`

## Contributing

The symbol database lives in `data/seed.sql`. If a package is missing, adding it is a one line SQL insert. Contributions welcome.