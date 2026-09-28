import pytest
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

def test_multiple_source_files():
    result = find_source_files(TESTDATA / "multiple_source_files")

    assert len(result) == 3
    assert {f.name for f in result} == {
        "main.cpp",
        "math.cpp",
        "math.h",
    }

def test_nested():
    result = find_source_files(TESTDATA / "nested")

    assert len(result) == 3
    assert {f.name for f in result} == {
        "main.cpp",
        "math.cpp",
        "math.h",
    }

def test_different_file_types():
    result = find_source_files(TESTDATA / "different_file_types")

    assert len(result) == 6
    assert {f.name for f in result} == {
        "main.cc",
        "math.cpp",
        "math.hpp",
        "low_level.c",
        "server.cxx",
        "server.h",
    }

def test_non_cpp_file_types():
    result = find_source_files(TESTDATA / "non_cpp_file_types")

    assert len(result) == 1
    assert {f.name for f in result} == {
        "main.cpp",
    }

def test_directory_not_found():
    with pytest.raises(FileNotFoundError, match="Directory not found"):
        find_source_files(Path("does_not_exist"))