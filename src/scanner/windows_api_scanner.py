from pathlib import Path
from dataclasses import dataclass

import re

@dataclass
class Finding:
    file: Path
    line: int
    symbol: str

WINDOWS_APIS: list[str] = [
    "windows.h",
    "CreateFileW",
    "CreateFileA",
    "GetModuleHandle",
    "GetModuleHandleA",
    "GetProcAddress",
    "LoadLibrary",
    "LoadLibraryW",
    "LoadLibraryA",
    "CreateProcess",
    "CreateNamedPipe",
    "GetLastError",
    "WaitForSingleObject",
    "Sleep",
    "DWORD",
    "HANDLE",
    "LPCTSTR",
]

def find_symbols(line: str) -> list[str]:
    return [
        symbol
        for symbol in WINDOWS_APIS
        if re.search(rf"\b{re.escape(symbol)}\b", line)
    ]

def scan_file(file: Path) -> list[Finding]:
    
    results = []

    with open(file) as f:
        for line_number, line in enumerate(f, start=1):
            for symbol in find_symbols(line):
                results.append(
                    Finding(
                        file=file,
                        line=line_number,
                        symbol=symbol,
                    )
                )
    
    return results

def scan_files(files: list[Path]) -> list[Finding]:

    results = []

    for file in files:
        results.extend(scan_file(file))

    # For deterministic results the result list is sorted
    results.sort(key=lambda f: (str(f.file), f.line, f.symbol))

    return results