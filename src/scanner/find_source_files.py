from pathlib import Path

def find_source_files(path: Path) -> list[Path]:

    source_files = []

    for file in path.rglob("*"):
        if file.is_file():
            if file.suffix in {".cpp", ".h", ".hpp", ".cc", ".cxx", ".c"}:
                source_files.append(file)

    return source_files