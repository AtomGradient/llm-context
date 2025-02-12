# LLM Context

<div align="center">

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/llm-context.svg)](https://badge.fury.io/py/llm-context)

🚀 A powerful command-line tool to combine multiple files into a single file formatted for Large Language Model (LLM) context.
</div>

## 🌟 Features

- 📁 Combine multiple files into a single document
- 🎯 Smart file pattern matching and exclusion
- 🎨 Markdown-formatted output with syntax highlighting
- 🔄 Preserve file structure and organization
- ⚡️ Fast and efficient processing
- 🛠 Customizable output formatting

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🚀 Installation

Install using pip:

```bash
pip install llm-context
```

Or install with pipx for isolated environments:

```bash
pipx install llm-context
```

## 💻 Usage

### Basic Usage

Simply point the tool to your project directory:

```bash
llm-context /path/to/project
```

### Advanced Usage

Customize the output with various options:

```bash
llm-context /path/to/project \
    --patterns "*.py" "*.js" \
    --exclude "__pycache__/*" "node_modules/*" \
    --output llmcontext.txt \
    --header "Project source code for review:" \
    --no-language
```

## 🎮 Command Options

| Option | Short | Description | Example |
|--------|-------|-------------|----------|
| `--patterns` | `-p` | File patterns to include (multiple allowed) | `--patterns "*.py" "*.js"` |
| `--exclude` | `-e` | Patterns to exclude (multiple allowed) | `--exclude "test/*" "*.pyc"` |
| `--output` | `-o` | Output file path | `--output combined.txt` |
| `--header` | `-h` | Optional header text | `--header "Source code:"` |
| `--language/--no-language` | - | Toggle language hints in code blocks | `--no-language` |

## 📝 Examples

### Combining Python and JavaScript Files

```bash
llm-context . \
    --patterns "*.py" "*.js" \
    --exclude "tests/*" \
    --header "Frontend and Backend Source Code:"
```

### Processing a Specific Directory

```bash
llm-context ./src \
    --patterns "*.ts" \
    --output typescript-code.txt \
    --language
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Thanks to all contributors who have helped shape this tool
- Inspired by the need for better LLM context management

---

<div align="center">
Made with ❤️ for the AI and developer community
</div>