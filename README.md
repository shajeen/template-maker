# Template Maker

[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://python.org)
[![PyPI](https://img.shields.io/pypi/v/template-maker.svg)](https://pypi.org/project/template-maker/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A powerful CLI tool for generating CMake + Conan project templates for C++ applications and libraries.

## Overview

Template Maker automates the creation of well-structured C++ projects with modern build systems. It generates complete project scaffolding including CMake configuration, Conan dependency management, and proper directory structure for both applications and libraries.

### Key Features

- 🚀 **Quick Setup**: Generate complete C++ project structure in seconds
- 📦 **Conan Integration**: Built-in support for modern C++ dependency management
- 🏗️ **CMake Ready**: Pre-configured CMake files for immediate development
- 📁 **Dual Modes**: Support for both application and library project types
- 🧪 **Test Framework**: Includes test structure and configuration
- ⚡ **Zero Configuration**: Works out of the box with sensible defaults

## Installation

### From PyPI (Recommended)

```bash
pip install template-maker
```

### From Source

```bash
pip install git+https://github.com/shajeen/template-maker.git
```

### Verify Installation

```bash
template-maker --help
```
  
## Usage

Template Maker requires two arguments:

- `--name`: Your project name
- `--ptype`: Project type (0 for application, 1 for library)

### Quick Start

#### Create a C++ Application

```bash
template-maker --name="my_awesome_app" --ptype=0
```

This generates:
```
out/my_awesome_app/
├── CMakeLists.txt
├── README.md
├── LICENSE
├── conanfile.txt
└── src/
    └── main.cpp
```

#### Create a C++ Library

```bash
template-maker --name="my_awesome_lib" --ptype=1
```

This generates:
```
out/my_awesome_lib/
├── CMakeLists.txt
├── README.md
├── LICENSE
├── app/                    # Example application
│   ├── CMakeLists.txt
│   └── src/
│       └── main.cpp
├── lib/                    # Library source
│   ├── CMakeLists.txt
│   ├── conanfile.py
│   ├── include/
│   │   └── main.h
│   └── src/
│       └── main.cpp
└── test/                   # Test framework
    ├── CMakeLists.txt
    ├── conanfile.txt
    └── src/
        └── main.cpp
```

### Project Types

| Type | Value | Description |
|------|-------|-------------|
| Application | 0 | Standalone executable project |
| Library | 1 | Reusable library with tests and example app |

### Building Generated Projects

After generation, navigate to the output directory and build:

```bash
cd out/your_project_name
mkdir build && cd build
conan install .. --build=missing
cmake ..
cmake --build .
```

## Requirements

- Python 3.6+
- Git (for installation from source)

## Examples

### Application Project Structure

The generated application includes:
- Modern CMake configuration
- Conan dependency management
- Source code organization
- Build scripts ready for immediate use

### Library Project Structure

The generated library includes:
- Separate lib, app, and test directories
- Header/source separation
- Conan package configuration
- Example application demonstrating library usage
- Test framework setup

## Roadmap

- [ ] Support for additional build systems (Meson, Bazel)
- [ ] Template customization options
- [ ] Integration with popular C++ frameworks
- [ ] Docker support
- [ ] CI/CD template generation

See the [open issues](https://github.com/shajeen/template-maker/issues) for a list of proposed features and known issues.

## Contributing

Contributions are welcome! Here's how you can help:

1. **Report Issues**: Found a bug? [Create an issue](https://github.com/shajeen/template-maker/issues/new)
2. **Suggest Features**: Have an idea? [Request a feature](https://github.com/shajeen/template-maker/issues/new)
3. **Submit Code**: 
   - Fork the repository
   - Create a feature branch
   - Make your changes with tests
   - Submit a pull request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Support

- 📧 Email: [shajeenahmed@gmail.com](mailto:shajeenahmed@gmail.com)
- 🐦 Twitter: [@shajeenahamed](https://twitter.com/shajeenahamed)
- 🐛 Issues: [GitHub Issues](https://github.com/shajeen/template-maker/issues)
- 📖 Documentation: [Project Wiki](https://github.com/shajeen/template-maker/wiki)

## Acknowledgments

- The C++ community for continuous innovation
- Conan team for excellent package management
- CMake developers for the robust build system

