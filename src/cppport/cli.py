import argparse
import sys

from pathlib import Path
from scanner.find_source_files import find_source_files
from scanner.windows_api_scanner import scan_files, Finding

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
            prog='cppport', 
            usage='%(prog)s [options]',
            description=(
                "A portability-focused linter for C++ projects "
                "that detects Windows-specific issues that hinder Linux compilation."
            ),
        )
    
    parser.add_argument('folder', type=Path, nargs="?")
    return parser

def run(folder: Path) -> list[Finding]: 
    try:
        files = find_source_files(folder)
    except FileNotFoundError:
        print(f"Directory {folder} not found.")
        raise sys.exit(2)  
    
    return scan_files(files)

def print_findings(findings: list[Finding]) -> None: 
    count = len(findings)

    if count == 1:
        print("Found 1 Windows API usage.")
    else:
        print(f"Found {count} Windows API usages")
    
    if count > 0:
        print("")

        for finding in findings:
            print(f"{finding.file}:{finding.line} {finding.symbol}")

def main() -> None:
    parser = create_parser()

    if len(sys.argv) == 1:
        parser.print_help()
        return

    args = parser.parse_args()

    findings = run(args.folder)
    print_findings(findings)

if __name__ == "__main__":
    main()