# Scripts & Tools

This directory contains helper scripts and automation tools for the project.

## Available Tools

### Python Tools

#### test_runner.py
Automated testing framework for pseudocode algorithms.

```bash
# Run tests
python scripts/test_runner.py tests/test_suma.json examples/suma.md
```

#### new_task.py
Interactive generator for creating new task files.

```bash
# Generate new task
python scripts/new_task.py
```

### PowerShell Script
**scripts.ps1** - PowerShell automation utilities for Windows

```powershell
# Run PowerShell script
.\scripts\scripts.ps1
```

### Makefile
**Makefile** - Build automation for Unix-like systems (Linux/macOS)

```bash
# Run make commands
make <target>
```

## Usage Examples

### Running Tests
```bash
# Single test
python scripts/test_runner.py tests/test_suma.json examples/suma.md

# Multiple tests
python scripts/test_runner.py tests/test_*.json examples/*.md
```

### Creating New Tasks
```bash
# Interactive mode
python scripts/new_task.py

# Follow the prompts to create a new task structure
```

## Back to Main

Return to [main README](../README.md)
