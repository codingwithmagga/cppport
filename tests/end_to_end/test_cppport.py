import subprocess
from pathlib import Path

# TODO: as pytest fixture to conftest.py, maybe rm subfolder "find_source_files"
TESTDATA = Path(__file__).parents[1] / "testdata" / "windows_api_scanner"

def test_cli_without_arguments():
    result = subprocess.run(
        ["cppport"],
        capture_output=True,
        text=True,
    )
    
    assert result.returncode == 0
    assert "usage" in result.stdout.lower()

def test_no_findings():
    result = subprocess.run(
        ["cppport", TESTDATA / "no_findings"],
        capture_output=True,
        text=True,
    )
            
    assert result.returncode == 0
    assert "found 0 windows api usages" in result.stdout.lower()

def test_one_source_file_windows_h():
    result = subprocess.run(
        ["cppport", TESTDATA / "one_source_file_windows_h"],
        capture_output=True,
        text=True,
    )
            
    assert result.returncode == 0
    assert "found 1 windows api usage" in result.stdout.lower()
    assert "found 1 windows api usage" in result.stdout.lower()

def test_multi_file_test():
    result = subprocess.run(
        ["cppport", TESTDATA / "multi_file_test"],
        capture_output=True,
        text=True,
    )
            
    assert result.returncode == 0
    assert "found 3 windows api usages" in result.stdout.lower()
    assert "found 3 windows api usages" in result.stdout.lower()

def test_one_source_file_multiple_findings():
    result = subprocess.run(
        ["cppport", TESTDATA / "one_source_file_multiple_findings"],
        capture_output=True,
        text=True,
    )
            
    assert result.returncode == 0
    assert "found 9 windows api usages" in result.stdout.lower()
    assert "found 9 windows api usages" in result.stdout.lower()

def test_non_existent_path():
    non_existent_path = TESTDATA / "non_existent_path"
    result = subprocess.run(
        ["cppport", non_existent_path],
        capture_output=True,
        text=True,
    )
            
    assert result.returncode == 2
    assert f"Directory {non_existent_path} not found." in result.stdout
