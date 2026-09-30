# cppport
A portability-focused linter for C++ projects that detects Windows-specific APIs, headers, compiler extensions, and other issues that hinder Linux compilation.

> 🚧 Early development project. APIs, output formats, and detection rules may change between releases.

## Motivation

Porting a C++ codebase from Windows to Linux often reveals hidden platform dependencies such as:

- Windows APIs
- Windows-only headers
- MSVC-specific compiler extensions
- Case-sensitivity issues in include paths
- Platform-specific third-party libraries

cppport aims to help developers identify these issues before starting a Linux port.

## Example Usage

```bash
cppport ./my_project
```

Example Output

```
Found 42 source files.
```

Future versions will provide detailed findings:

```
CRITICAL  src/platform/file.cpp:23
          CreateFileW()

WARNING   include/platform.h:8
          windows.h

INFO      src/main.cpp:42
          Code protected by #ifdef _WIN32
```

## Scope

cppport focuses on one question:

>What prevents this C++ project from compiling on Linux?

The initial goal is compilation portability, not runtime correctness.

### In Scope

* Windows API usage
* Windows-only headers
* MSVC compiler extensions
* Include case-sensitivity issues
* Platform-specific library dependencies

### Out of Scope (for now)
* Runtime behavior differences
* Automatic code migration
* Build system generation
* Full C++ semantic analysis
* Clang AST integration

## Technical Approach

cppport currently performs lightweight text-based analysis.

### Current Limitations

The tool does not currently:

* Evaluate preprocessor conditions
* Expand macros
* Parse C++ syntax
* Build an AST
* Compile source code

Findings should therefore be interpreted as indicators rather than compiler diagnostics.

## Development Status

This project is in very early development.

Current functionality:

* Command-line interface
* Recursive source file discovery
* Unit tests
* End-to-end tests
* Continuous integration pipeline

Planned functionality:

* Windows API detection
* Windows-only header detection
* Compiler extension checks
* Include case-sensitivity validation
* Configurable rule system
* Structured reports


## Development

Install:
```bash
pip install -e .
```

Run:
```bash
cppport <project-path>
```

Tests:
```bash
pytest
```

Lint:
```bash
ruff check .
```

## Roadmap

### v0.0.1

* CLI skeleton
* Recursive source file discovery
* Unit tests
* End-to-end tests
* CI pipeline

### v0.0.2

* Windows API detection

### v0.0.3

* Ifdef-aware analysis

### v0.0.4

* Windows-only header database

### v0.1.0

* First stable MVP release

## License

Apache License 2.0


## Non-Goals

cppport is not intended to replace:

- clang-tidy
- Clang diagnostics
- Compiler warnings
- Static analyzers

Instead, cppport complements those tools by focusing specifically on Linux portability issues.
