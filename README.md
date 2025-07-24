# 🔧 Krypton – Product Requirements Document (PRD)

**Version:** v0.1
**Date:** 2025-07-24
**Author:** \[Konvotech]

---

## 1. 📌 Product Overview

**Krypton** is a beginner-friendly, Turkish-localized programming language that is a subset of Python. It retains Python’s syntax while replacing English keywords and built-in functions with Turkish equivalents. `.kr` source files are transpiled into Python code and executed within a bundled virtual environment. The main goal is to lower the barrier of entry to programming for Turkish-speaking newcomers.

---

## 2. 🎯 Target Audience

* First-time programmers with no English background
* High school and university students
* Individuals interested in coding literacy
* Anyone intimidated by English-heavy programming environments

---

## 3. 🧱 Features

### 3.1 Language Features

* Turkish keywords (`eğer`, `iken`, `tanım`, `yazdır`)
* Turkish built-ins (`uzunluk()`, `aralık()`, `liste()`)
* Python-compatible syntax (indentation-based, colon usage)
* `.kr` file extension
* Simplified, beginner-friendly error messages (in Turkish)

### 3.2 Transpilation

* `.kr` files are transpiled to `.py` (Python 3)
* `krypton build file.kr` generates a `.py` output
* `krypton run file.kr` compiles and runs directly

### 3.3 Standard Library

* Custom `kstd` (Krypton Standard Library)
* Turkish-named helper APIs (`oku_dosya`, `zaman.now()`, `yaz()`)
* Bundled within an isolated Python virtual environment
* Bridges to Python standard modules as needed

### 3.4 CLI Tool

* Command-line interface: `krypton`

  * Commands: `build`, `run`, `help`, `show-output`, `explain-error`
* Auto-compiles `.kr` files
* Optional output display of transpiled Python code
* Turkish error messages and usage tips

---

## 4. 🔧 Technical Architecture

| Component         | Description                                                            |
| ----------------- | ---------------------------------------------------------------------- |
| **Lexer/Parser**  | Custom syntax parser using `lark` or `ply`                             |
| **Transpiler**    | Token mapping + optional AST transformation                            |
| **Runtime**       | Embedded Python 3.10+ virtual environment                              |
| **CLI Interface** | Built with `Typer` or `Click`                                          |
| **Packaging**     | Delivered via PyInstaller or zipapp                                    |
| **Modules**       | `kstd` folder contains Turkish-friendly modules (e.g., `kstd/file.py`) |

---

## 5. ✅ MVP Scope (Minimum Viable Product)

* Core language constructs: `eğer`, `değilse`, `iken`, `her`, `tanım`
* Basic built-in functions: `yazdır()`, `uzunluk()`, `aralık()`
* `krypton build` and `krypton run` commands
* `kstd` library with at least 5 core modules
* Turkish-language error messages and a `help()` system

---

## 6. 📦 Example Project Structure

```
my_project/
├── hello.kr
├── krypton/
│   ├── lexer.py
│   ├── parser.py
│   ├── transpiler.py
│   ├── cli.py
│   └── kstd/
│       ├── time.py
│       ├── file.py
│       └── string.py
└── venv/
```