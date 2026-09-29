import subprocess
from pathlib import Path

# TODO: as pytest fixture to conftest.py, maybe rm subfolder "find_source_files"
TESTDATA = Path(__file__).parents[1] / "testdata" / "find_source_files"

def test_cli_without_arguments():
    result = subprocess.run(
        ["cppport"],
        capture_output=True,
        text=True,
    )
    
    assert result.returncode == 0
    assert "usage" in result.stdout.lower()

def test_one_source_file():
    result = subprocess.run(
        ["cppport", TESTDATA / "one_source_file"],
        capture_output=True,
        text=True,
    )
            
    assert result.returncode == 0
    assert "found 1 source file." in result.stdout.lower()

def test_multiple_source_files():
    result = subprocess.run(
        ["cppport", TESTDATA / "multiple_source_files"],
        capture_output=True,
        text=True,
    )
            
    assert result.returncode == 0
    assert "found 3 source files." in result.stdout.lower()

def test_non_existent_path():
    non_existent_path = TESTDATA / "non_existent_path"
    result = subprocess.run(
        ["cppport", non_existent_path],
        capture_output=True,
        text=True,
    )
            
    assert result.returncode == 2
    assert f"Directoy {non_existent_path} not found." in result.stdout