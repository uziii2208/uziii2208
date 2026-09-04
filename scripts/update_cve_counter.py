import re
import sys
from pathlib import Path

README_PATH = Path(__file__).resolve().parent.parent / "CVEs_updating" / "README.md"

MARKERS = {
    "TOTAL": "TOTAL",
    "CRITICAL": "CRITICAL",
    "HIGH": "HIGH",
    "MEDIUM": "MEDIUM",
    "LOW": "LOW",
}

SEVERITY_PATTERNS = {
    "CRITICAL": r"!\[Critical\]",
    "HIGH": r"!\[High\]",
    "MEDIUM": r"!\[Medium\]|!\[Normal\]",
    "LOW": r"!\[Low\]",
}


def count_advisories(content: str) -> dict[str, int]:
    lines = content.splitlines()
    advisory_lines = [l for l in lines if "| [GHSA-" in l]

    counts = {"TOTAL": len(advisory_lines)}
    for severity, pattern in SEVERITY_PATTERNS.items():
        counts[severity] = sum(
            1 for l in advisory_lines if re.search(pattern, l)
        )
    return counts


def update_markers(content: str, counts: dict[str, int]) -> str:
    for key, label in MARKERS.items():
        pattern = rf"(<!-- {label}_START -->)\d+(<!-- {label}_END -->)"
        replacement = rf"\g<1>{counts[key]}\g<2>"
        content = re.sub(pattern, replacement, content)
    return content


def main() -> None:
    if not README_PATH.exists():
        print(f"ERROR: {README_PATH} not found")
        sys.exit(1)

    content = README_PATH.read_text(encoding="utf-8")
    counts = count_advisories(content)

    print("=== CVE Advisory Counter ===")
    for label, count in counts.items():
        print(f"  {label}: {count}")

    updated = update_markers(content, counts)

    if updated != content:
        README_PATH.write_text(updated, encoding="utf-8")
        print("\nREADME.md updated successfully.")
    else:
        print("\nNo changes needed.")


if __name__ == "__main__":
    main()
