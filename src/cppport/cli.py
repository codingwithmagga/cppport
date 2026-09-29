import argparse

from pathlib import Path
from scanner.find_source_files import find_source_files

def main() -> None:
    parser = argparse.ArgumentParser(
        prog='cppport', 
        usage='%(prog)s [options]',
        description='A portability-focused linter for C++ projects that detects Windows-specific issues that hinder Linux compilation.',
    )
    
    parser.add_argument('folder', type=Path, nargs="?")

    args = parser.parse_args()

    if not args.folder:
        parser.print_help()
        raise SystemExit(0)

    files = find_source_files(args.folder)

    print(f"Found {len(files)} source file.")

if __name__ == "__main__":
    main()