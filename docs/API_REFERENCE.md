# API Reference

## Command Line Interface

### Basic Usage

```bash
template-maker --name <project_name> --ptype <project_type>
```

### Arguments

#### Required Arguments

| Argument | Type | Description | Values |
|----------|------|-------------|--------|
| `--name` | string | Project name for the generated template | Any valid directory name |
| `--ptype` | integer | Project type to generate | `0` (application) or `1` (library) |

### Examples

#### Application Project
```bash
template-maker --name="my_calculator" --ptype=0
```

#### Library Project
```bash
template-maker --name="math_utils" --ptype=1
```

## Python API

### Module Structure

```python
from template_maker.main import main, empty_project_argument, create_structure
```

### Functions

#### `main()`
Entry point for the command-line interface.

#### `empty_project_argument(empty_project, project_name)`
Generates project structure based on type and name.

**Parameters:**
- `empty_project` (int): Project type (0 for app, 1 for library)
- `project_name` (str): Name of the project

#### `create_structure(config_file, project_name, option_type)`
Creates the directory structure and files based on configuration.

**Parameters:**
- `config_file` (str): Path to JSON configuration file
- `project_name` (str): Name of the project
- `option_type` (int): Project type

#### `replace_test_in_file(file, from_text, to_text)`
Utility function for text replacement in generated files.

**Parameters:**
- `file` (str): File path
- `from_text` (str): Text to replace
- `to_text` (str): Replacement text

### Configuration Files

Template Maker uses JSON configuration files to define project structures:

- `conan_application.json`: Application project template
- `conan_library.json`: Library project template

### Output Structure

All generated projects are created in the `out/` directory with the following pattern:
```
out/
└── <project_name>/
    └── [generated files and directories]
```