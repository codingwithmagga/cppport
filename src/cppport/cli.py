import argparse
import sys

from pathlib import Path
from scanner.find_source_files import find_source_files
from scanner.windows_api_scanner import scan_files

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

def main() -> None:
    parser = create_parser()

    if len(sys.argv) == 1:
        parser.print_help()
        return

    args = parser.parse_args()

    if not args.folder:
        parser.print_help()
        raise sys.exit(0)

    try:
        files = find_source_files(args.folder)
    except FileNotFoundError:
        print(f"Directory {args.folder} not found.")
        raise sys.exit(2)  
    
    findings = scan_files(files)
    
    count = len(findings)

    if count == 1:
        print("Found 1 Windows API usage.")
    else:
        print(f"Found {count} Windows API usages")
    
    if count > 0:
        print("")

        for finding in findings:
            print(f"{finding.file}:{finding.line} {finding.symbol}")

if __name__ == "__main__":
    main()