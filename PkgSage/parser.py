import re

PATTERNS = {
    "CS0246": re.compile(
        r"error CS0246: The type or namespace name '(\w+)'.*could not be found"
    ),
    "CS0234": re.compile(
        r"error CS0234: The type or namespace name '(\w+)' does not exist in the namespace '([\w.]+)'"
    ),
    "CS0012": re.compile(
        r"error CS0012: The type '([\w.<>]+)' is defined in an assembly that is not referenced"
    ),
}

def parse_errors(build_output: str) -> list[dict]:
    errors = []
    seen = set()

    for line in build_output.splitlines():
        for code, pattern in PATTERNS.items():
            m = pattern.search(line)
            if m:
                symbol = m.group(1)
                namespace = m.group(2) if code == "CS0234" else None

                # skip duplicates - same symbol can appear 20 times across files
                key = (code, symbol, namespace)
                if key in seen:
                    continue
                seen.add(key)

                errors.append({
                    "code": code,
                    "symbol": symbol,
                    "namespace": namespace,
                    "raw": line.strip(),
                })

    return errors
