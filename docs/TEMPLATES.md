# Template Documentation

## Template System Overview

Template Maker uses a JSON-based configuration system to define project structures. Each project type has its own configuration file that specifies folders to create, files to copy, and text replacements to perform.

## Template Types

### Application Template (`ptype=0`)

**Configuration:** `conan_application.json`

Generates a simple C++ application with:
- Main source file
- CMake configuration
- Conan dependency management
- Basic project structure

**Generated Structure:**
```
project_name/
├── CMakeLists.txt
├── README.md
├── LICENSE
├── conanfile.txt
└── src/
    └── main.cpp
```

### Library Template (`ptype=1`)

**Configuration:** `conan_library.json`

Generates a complete C++ library project with:
- Library source and headers
- Example application
- Test framework
- Conan package configuration

**Generated Structure:**
```
project_name/
├── CMakeLists.txt
├── README.md
├── LICENSE
├── app/                    # Example application
│   ├── CMakeLists.txt
│   └── src/
│       └── main.cpp
├── lib/                    # Library implementation
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

## Configuration File Format

### Structure

```json
{
  "folder": [
    {
      "name": "folder_name",
      "target": "path/to/parent/"
    }
  ],
  "file": [
    {
      "name": "filename.ext",
      "path": "template/source/path",
      "target": "destination/path/"
    }
  ]
}
```

### Fields

#### Folder Objects
- `name`: Name of the folder to create
- `target`: Parent directory path (relative to project root)

#### File Objects
- `name`: Final name of the file in the generated project
- `path`: Source file path in the template directory
- `target`: Destination directory path (relative to project root)

## Template Files

Template files are stored in `template_maker/configuration/template/` and contain placeholder text that gets replaced during generation.

### Placeholder Replacements

| Placeholder | Replaced With | Context |
|-------------|---------------|---------|
| `example` | Project name | All files |
| `exampleApp` | Project name + "App" | Library CMakeLists.txt |
| `exampleLib` | Project name + "Lib" | Library CMakeLists.txt, conanfile.py |
| `exampleTest` | Project name + "Test" | Library CMakeLists.txt |
| `exampleConan` | Project name + "Conan" | Library conanfile.py |

### Example Template Files

#### CMakeLists.txt Template
```cmake
cmake_minimum_required(VERSION 3.15)
project(example)

set(CMAKE_CXX_STANDARD 17)

# Add executable
add_executable(${PROJECT_NAME} src/main.cpp)
```

After replacement for project "MyApp":
```cmake
cmake_minimum_required(VERSION 3.15)
project(MyApp)

set(CMAKE_CXX_STANDARD 17)

# Add executable
add_executable(${PROJECT_NAME} src/main.cpp)
```

## Adding Custom Templates

### Step 1: Create Template Files

Create your template files in `template_maker/configuration/template/`:

```
template/
├── my_custom_template/
│   ├── CMakeLists.txt
│   ├── src/
│   │   └── main.cpp
│   └── include/
│       └── header.h
```

### Step 2: Create Configuration File

Create a JSON configuration file:

```json
{
  "folder": [
    {"name": "src", "target": ""},
    {"name": "include", "target": ""}
  ],
  "file": [
    {
      "name": "CMakeLists.txt",
      "path": "template/my_custom_template/CMakeLists.txt",
      "target": ""
    },
    {
      "name": "main.cpp",
      "path": "template/my_custom_template/src/main.cpp",
      "target": "src/"
    },
    {
      "name": "header.h",
      "path": "template/my_custom_template/include/header.h",
      "target": "include/"
    }
  ]
}
```

### Step 3: Update Main Script

Modify `main.py` to support the new template:

```python
def empty_project_argument(empty_project, project_name):
    option_type = empty_project
    config_file = ""

    here = os.path.dirname(os.path.abspath(__file__))
    if option_type == 0:
        config_file = os.path.join(here,'configuration/conan_application.json')
    elif option_type == 1:
        config_file = os.path.join(here,'configuration/conan_library.json')
    elif option_type == 2:  # New template type
        config_file = os.path.join(here,'configuration/my_custom_template.json')

    create_structure(config_file, project_name, option_type)
```

## Best Practices

### Template Design

1. **Keep it Simple**: Templates should provide a good starting point without being overly complex
2. **Follow Conventions**: Use standard directory layouts and naming conventions
3. **Include Documentation**: Every template should include README and basic documentation
4. **Test Thoroughly**: Ensure generated projects build and run correctly

### File Organization

1. **Logical Structure**: Organize files in a way that makes sense for the project type
2. **Separation of Concerns**: Keep source, headers, tests, and documentation separate
3. **Build System Integration**: Ensure CMake and Conan files are properly configured

### Placeholder Usage

1. **Consistent Naming**: Use clear, descriptive placeholder names
2. **Minimal Replacements**: Only replace what's necessary
3. **Context Awareness**: Consider where replacements make sense

## Troubleshooting

### Common Issues

1. **File Not Found**: Check that template file paths in JSON are correct
2. **Build Errors**: Verify CMake and Conan configurations are valid
3. **Missing Directories**: Ensure all required folders are defined in JSON

### Debugging Templates

1. Generate a test project
2. Check the `out/` directory for correct structure
3. Try building the generated project
4. Verify all placeholders were replaced correctly