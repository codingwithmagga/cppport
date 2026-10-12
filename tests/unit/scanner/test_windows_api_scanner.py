from scanner.windows_api_scanner import scan_files
from pathlib import Path

# TODO: as pytest fixture to conftest.py
TESTDATA = Path(__file__).parents[2] / "testdata" / "windows_api_scanner"

def test_empty_file():
    testfile = TESTDATA / "empty_file" / "main.cpp"
    result = scan_files([testfile])
    assert result == []


def test_single_file_windows_h():

    testfile = TESTDATA / "one_source_file_windows_h" / "main.cpp"

    result = scan_files([testfile])

    assert len(result) == 1
    assert result[0].file == testfile
    assert result[0].line == 1
    assert result[0].symbol == "windows.h"

def test_single_file_multiple_findings():

    testfile = TESTDATA / "one_source_file_multiple_findings" / "main.cpp"

    result = scan_files([testfile])

    print(result)

    assert len(result) == 9

    assert [(f.line, f.symbol) for f in result] == [
        (1, "windows.h"),
        (4, "CreateFileA"),
        (7, "CreateFileW"),
        (10, "LoadLibraryA"),
        (11, "LoadLibraryW"),
        (13, "GetModuleHandleA"),
        (14, "GetProcAddress"),
        (14, "CreateFileW"),
        (14, "GetModuleHandleA"),
    ]