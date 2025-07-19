# Development Guide

## Setting Up Development Environment

### Prerequisites

- Python 3.6 or higher
- Git
- Text editor or IDE (VS Code, PyCharm recommended)

### Clone and Setup

```bash
git clone https://github.com/shajeen/template-maker.git
cd template-maker

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

### Project Structure

```
template-maker/
├── template_maker/           # Main package
│   ├── __init__.py
│   ├── main.py              # CLI entry point
│   └── configuration/       # Template configurations
│       ├── conan_application.json
│       ├── conan_library.json
│       └── template/        # Template files
├── sample_output/           # Example generated projects
├── docs/                    # Documentation
├── pyproject.toml          # Project configuration
├── README.md
├── LICENSE
├── CONTRIBUTING.md
└── CODE_OF_CONDUCT.md
```

## Configuration System

### Template Configuration

Templates are defined in JSON files that specify:
- Folder structure to create
- Files to copy and their destinations
- Text replacements to perform

#### Configuration Format

```json
{
  "folder": [
    {
      "name": "src",
      "target": ""
    }
  ],
  "file": [
    {
      "name": "main.cpp",
      "path": "template/app/main.cpp",
      "target": "src/"
    }
  ]
}
```

### Adding New Templates

1. Create template files in `template_maker/configuration/template/`
2. Create a new JSON configuration file
3. Update `main.py` to support the new template type

### Template Variables

The following placeholders are automatically replaced:
- `example` → Project name
- `exampleApp` → Project name + "App" (libraries only)
- `exampleLib` → Project name + "Lib" (libraries only)
- `exampleTest` → Project name + "Test" (libraries only)
- `exampleConan` → Project name + "Conan" (libraries only)

## Testing

### Manual Testing

```bash
# Test application generation
template-maker --name="test_app" --ptype=0

# Test library generation
template-maker --name="test_lib" --ptype=1

# Verify generated projects build correctly
cd out/test_app
mkdir build && cd build
conan install .. --build=missing
cmake ..
cmake --build .
```

### Automated Testing

Currently, the project relies on manual testing. Future improvements should include:
- Unit tests for configuration parsing
- Integration tests for project generation
- Build verification tests

## Code Style

### Python Style Guidelines

- Follow PEP 8
- Use meaningful variable names
- Add docstrings for functions
- Keep functions focused and small

### Example Code Style

```python
def create_structure(config_file, project_name, option_type):
    """Create project structure based on configuration.
    
    Args:
        config_file (str): Path to JSON configuration file
        project_name (str): Name of the project
        option_type (int): Project type (0=app, 1=library)
    """
    with open(config_file) as file:
        data = json.load(file)
    # Implementation...
```

## Release Process

### Version Management

Versions are managed through `pyproject.toml` and Git tags.

### Publishing to PyPI

1. Update version in `pyproject.toml`
2. Create release commit
3. Tag the release: `git tag v1.x.x`
4. Push tags: `git push --tags`
5. Build and publish: `python -m flit publish`

## Common Development Tasks

### Adding a New Project Type

1. Create template files in `configuration/template/`
2. Create JSON configuration file
3. Update `empty_project_argument()` function
4. Update CLI help text and documentation
5. Test the new template

### Modifying Existing Templates

1. Edit files in `configuration/template/`
2. Update corresponding JSON configuration if needed
3. Test with sample projects
4. Verify builds work correctly

### Debugging

Use Python's built-in debugging tools:

```python
import pdb; pdb.set_trace()  # Add breakpoint
```

Or run with verbose output:

```bash
python -c "
import template_maker.main as tm
tm.empty_project_argument(0, 'debug_test')
"
```