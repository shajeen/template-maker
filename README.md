# internal-tools

#### Usage
```[bash]
╰─⠠⠵ python code-available-internal-tools.py --h
usage: code-available-internal-tools.py [-h] [--project_name PROJECT_NAME] [--empty_project {0,1}]

Internal tools

optional arguments:
  -h, --help            show this help message and exit
  --project_name PROJECT_NAME
                        Enter project name
  --empty_project {0,1}
                        Create empty project structure, ({0} - conan CMake app structure), ({1} - conan CMake lib structure)
```

**To create CMake conan application structure**
```[bash]
python code-available-internal-tools.py --project_name=sampleApplication --empty_project=0
```

**To create CMake conan library structure**
```[bash]
python code-available-internal-tools.py --project_name=sampleLibrary --empty_project=1
```
