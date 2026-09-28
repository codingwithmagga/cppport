from pathlib import Path

from scanner.find_source_files import find_source_files

# später als pytest fixture nach conftest.py
TESTDATA = Path(__file__).parents[2] / "testdata" / "find_source_files"

def test_empty_dir():
    result = find_source_files(TESTDATA / "empty_dir")
    assert result == []