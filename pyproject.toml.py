[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.backends.legacy:build"

[project]
name = "pkgsage"
version = "0.1.0"
description = "CLI tool that analyses .NET build errors and suggests the NuGet package most likely to fix them"
readme = "README.md"
requires-python = ">=3.11"
license = {text = "MIT"}
dependencies = [
    "platformdirs>=4.0",
]

[project.scripts]
pkgsage = "PkgSage.cli:main"

[tool.setuptools.packages.find]
where = ["."]
include = ["PkgSage*"]