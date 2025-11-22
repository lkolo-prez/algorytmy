<div align="center">

# Pseudocode Learning Environment

**Interactive environment for writing, testing, and debugging algorithms in educational pseudocode**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![CI Status](https://img.shields.io/badge/CI-passing-brightgreen.svg)](.github/workflows/ci.yml)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[Quick Start](#quick-start) • [Features](#features) • [Examples](#examples) • [Documentation](#documentation) • [Problem Sets](workspace/) • [Contributing](#contributing)

</div>

---

## Features

This is a **complete learning environment** for algorithm education in pseudocode:

| Feature | Description |
|---------|-------------|
| **Syntax Validator** | Checks pseudocode correctness with detailed error messages |
| **Interpreter** | Executes pseudocode step-by-step with full variable tracking |
| **Debugger** | Visual step-through execution with state inspection |
| **Automated Testing** | JSON-based test framework for algorithm verification |
| **VS Code Integration** | Syntax highlighting, 27+ snippets, keyboard shortcuts |
| **Rich Examples** | 5+ fully tested example algorithms |
| **Comprehensive Docs** | Complete guides, tutorials, and cheat sheets |

---

## Installation

### Prerequisites
- Python 3.9 or higher
- VS Code (recommended)

### Setup

```bash
# Clone the repository
git clone https://github.com/lkolo-prez/algorytmy.git
cd algorytmy

# No additional dependencies needed - pure Python!

# Open in VS Code for best experience
code .
```

---

## Quick Start

### 1. Try an Example

```bash
# Run an example algorithm
python interpreter.py examples/suma.md --input=5,1,2,3,4,5

# Output: Suma = 15
```

### 2. Debug Step-by-Step

```bash
python interpreter.py examples/suma.md --input=5,1,2,3,4,5 --debug
```

```
URUCHOMIENIE: SumaElementow(A, n)
[Krok 1] read(n)
READ: n ← 5
[Krok 2] for i ← 1 to n do {
...
ZAKOŃCZONO
Kroki: 31
```

### 3. Write Your Own Algorithm

Create `workspace/my_first.md`:

```markdown
# My First Algorithm

```pseudocode
algorithm Greeting(name) {
read(name)
write("Hello, ", name, "!")
return 1
}
```
```

### 4. Validate & Run

```bash
# Validate syntax
python validator.py workspace/my_first.md

# Run it
python interpreter.py workspace/my_first.md --input=Alice --debug
```

---

## Project Structure

```
algorytmy/
Core Tools (Main Directory)
interpreter.py # Pseudocode interpreter
validator.py # Syntax validator
requirements.txt # Python dependencies
LICENSE # MIT License
README.md # This file

workspace/ # Your learning space
lista_1/ # Problem Set 1 (9 tasks)
lista_2/ # Problem Set 2 (11 tasks)
lista_3/ # Problem Set 3 (12 tasks)
README.md # Workspace guide

examples/ # Example algorithms with tests
suma.md # Array sum
min_max.md # Find min/max
sortowanie_babelkowe.md # Bubble sort
wyszukiwanie_binarne.md # Binary search
silnia.md # Factorial (recursive)

tests/ # Automated test cases (JSON)
test_suma.json
test_min_max.json
...

scripts/ # Helper tools & automation
test_runner.py # Test automation
new_task.py # File generator
scripts.ps1 # PowerShell automation
Makefile # Build automation
README.md # Scripts guide

docs/ # Documentation
README.md # Documentation index
README_EN.md # English documentation
README_PL.md # Polish documentation
CONTRIBUTING.md # Contribution guide
SCIAGAWKA.html # Printable cheat sheet
PRZEWODNIK_SRODOWISKA.md # Detailed guide (PL)
NAWIGACJA.md # Navigation guide
REORGANIZACJA.md # Reorganization notes
Lista 1.pdf # Course materials
Lista 2.pdf
Lista 3.pdf
Algorytmy - informacje.pdf

.vscode/ # VS Code configuration
pseudocode.tmLanguage.json # Syntax highlighting
pseudocode.code-snippets # 27 code snippets
tasks.json # Build tasks
keybindings.json # Keyboard shortcuts
```

---

## Tools Overview

### **Validator** - Check Syntax (MOST IMPORTANT!)

```bash
# Single file
python validator.py <file.md>

# Multiple files
python validator.py workspace/lista_1/*/zadanie.md

# VS Code: Ctrl+Shift+V
```

**Validates:**
- Braces `{ }` (not `end if/for/while`)
- Assignment operator `←` (not `=`)
- Keywords: `then`, `do`, `algorithm`
- Matching braces
- Array indexing (from 1)

### **Interpreter** - Execute Pseudocode

```bash
# Basic execution
python interpreter.py <file.md> --input=value1,value2,...

# Debug mode (step-by-step)
python interpreter.py <file.md> --input=values --debug
```

**Supports:**
- Variables and arrays (1D, 2D)
- Loops: `for`, `while`
- Conditionals: `if/else`
- Recursion
- I/O: `read()`, `write()`
- All arithmetic and logical operators

### **Test Runner** - Automated Testing

```bash
python scripts/test_runner.py <test.json> <algorithm.md>
```

### **File Generator** - Create New Tasks

```bash
python scripts/new_task.py # Interactive
```

---

## Pseudocode Syntax

### Algorithm Structure

```pseudocode
algorithm AlgorithmName(parameters) {
// Code here
}
```

### Assignment (NOT `=` !)

```pseudocode
variable ← value // Correct
variable = value // Wrong! (= is for comparison)
```

### Conditionals

```pseudocode
if condition then {
statements
} else {
statements
}
```

### Loops

```pseudocode
for i ← 1 to n do {
statements
}

while condition do {
statements
}
```

### Arrays (indexed from 1!)

```pseudocode
A[i] // 1D array
A[i, j] // 2D array
```

### I/O

```pseudocode
read(variable)
write("Text", variable)
```

**Full syntax guide:** [docs/SCIAGAWKA.html](docs/SCIAGAWKA.html) (printable cheat sheet)

---

## VS Code Snippets

Type these prefixes and press **Tab**:

| Prefix | Expands To |
|--------|------------|
| `alg` | Algorithm template |
| `if` / `ife` | If statement / If-else |
| `for` / `while` | Loops |
| `read` / `write` | I/O operations |
| `binsearch` | Binary search |
| `bubblesort` | Bubble sort |
| `fibonacci` | Fibonacci sequence |
| `factorial` | Factorial (recursive) |

**All 27 snippets:** [docs/DEMO_SNIPPETS.md](docs/DEMO_SNIPPETS.md)

---

## Examples

### Sum of Array Elements

```pseudocode
algorithm SumaElementow(A, n) {
read(n)
for i ← 1 to n do {
read(A[i])
}

suma ← 0
for i ← 1 to n do {
suma ← suma + A[i]
}

write("Suma = ", suma)
return suma
}
```

**Run it:**
```bash
python interpreter.py examples/suma.md --input=5,1,2,3,4,5
# Output: Suma = 15
```

### More Examples

- **[min_max.md](examples/min_max.md)** - Find minimum and maximum
- **[wyszukiwanie_binarne.md](examples/wyszukiwanie_binarne.md)** - Binary search
- **[sortowanie_babelkowe.md](examples/sortowanie_babelkowe.md)** - Bubble sort
- **[silnia.md](examples/silnia.md)** - Factorial (recursive)

All examples include:
- Full source code
- Complexity analysis
- Explanation
- Automated tests

---

## Running Tests

```bash
# Run all tests
python test_runner.py tests/test_suma.json examples/suma.md
python test_runner.py tests/test_min_max.json examples/min_max.md
python test_runner.py tests/test_sortowanie_babelkowe.json examples/sortowanie_babelkowe.md
python test_runner.py tests/test_wyszukiwanie_binarne.json examples/wyszukiwanie_binarne.md
python test_runner.py tests/test_silnia.json examples/silnia.md
```

All tests should pass with: ** Wszystkie testy przeszły pomyślnie!**

---

## Learning Workflow

### For Students

1. ** Study examples** - Start with `examples/suma.md`
```bash
python interpreter.py examples/suma.md --input=5,1,2,3,4,5 --debug
```

2. ** Work on problem sets** - Tasks in `workspace/lista_1/`, `lista_2/`, `lista_3/`
- Each task has `zadanie.md` (pseudocode) and `opis.md` (description)
- Total: 32 tasks (9 + 11 + 12)

3. ** Validate** - Check syntax (VERY IMPORTANT!)
```bash
python validator.py workspace/lista_1/1_suma_elementow/zadanie.md
```

4. ** Run & Debug** - Test with real data
```bash
python interpreter.py workspace/lista_1/1_suma_elementow/zadanie.md --input=values --debug
```

5. ** Add tests** - Create JSON test files in `tests/`
```bash
python scripts/test_runner.py tests/test_yours.json workspace/your_task/zadanie.md
```

### For Educators

- Use `examples/` as teaching material
- Students work in `workspace/lista_1/2/3/` with 32 ready tasks
- Create custom test cases in `tests/`
- All tools work offline - no internet needed
- **validator.py** is the most important tool for checking correctness

---

## Contributing

We welcome contributions! See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

### Quick Contribution Ideas

- Add more example algorithms
- Create more test cases
- Translate documentation
- Report bugs
- Suggest features
- Improve documentation

---

## License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file.

**TL;DR:** You can use, modify, and distribute this project freely, even commercially!

---

## Acknowledgments

- **Syntax Definition:** Based on conventions by **Mariusz Sobol** (Pedagogical University of Krakow)
- **Educational Purpose:** Created for "Algorithms and Data Structures" course
- **Open Source:** Made freely available for the education community

---

## Support

- **Documentation:** [docs/PRZEWODNIK_SRODOWISKA.md](docs/PRZEWODNIK_SRODOWISKA.md)
- **Issues:** [GitHub Issues](https://github.com/lkolo-prez/algorytmy/issues)
- **Discussions:** [GitHub Discussions](https://github.com/lkolo-prez/algorytmy/discussions)
- **Contact:** Open an issue with the `question` label

---

## Star This Project

If this project helps you learn algorithms, please **star it** on GitHub! 

It helps others discover this educational resource.

---

<div align="center">

**Made with for algorithm education**

**Happy Learning! **

[ Back to Top](#-pseudocode-learning-environment)

</div>
