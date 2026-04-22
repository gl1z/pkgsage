import subprocess

def run_build(project_path: str) -> tuple[int, str]:
    result = subprocess.run(
        ["dotnet", "build", project_path],
        capture_output=True,
        text=True,
    )
    # dotnet writes errors to stdout not stderr, combine both just in case
    return result.returncode, result.stdout + result.stderr