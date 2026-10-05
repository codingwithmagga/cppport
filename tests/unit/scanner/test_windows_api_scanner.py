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