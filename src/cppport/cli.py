import argparse
import sys

from pathlib import Path
from scanner.find_source_files import find_source_files
from scanner.windows_api_scanner import scan_files, Finding

SUCCESS = 0
ERROR_DIRECTORY_NOT_FOUND = 2

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

def print_findings(findings: list[Finding]) -> None: 
    count = len(findings)

    if count == 1:
        print("Found 1 Windows API usage.")
    else:
        print(f"Found {count} Windows API usages")
    
    if count == 0:
        return

    print("")
    for finding in findings:
        print(f"{finding.file}:{finding.line} {finding.symbol}")

def run(folder: Path) -> int: 
    try:
        files = find_source_files(folder)
    except FileNotFoundError:
        print(f"Directory {folder} not found.")
        return ERROR_DIRECTORY_NOT_FOUND 

    findings = scan_files(files)
    print_findings(findings)
    
    return SUCCESS

def main() -> None:
    parser = create_parser()

    if len(sys.argv) == 1:
        parser.print_help()
        return SUCCESS

    args = parser.parse_args()
    
    return run(args.folder)

if __name__ == "__main__":
     raise SystemExit(main())