from pathlib import Path

from scanner.find_source_files import find_source_files

# TODO: as pytest fixture to conftest.py
TESTDATA = Path(__file__).parents[2] / "testdata" / "find_source_files"

def test_empty_dir():
    result = find_source_files(TESTDATA / "empty_dir")
    assert result == []

def test_one_source_file():
    result = find_source_files(TESTDATA / "one_source_file")
    assert len(result) == 1
    assert result[0].name == "main.cpp"