# internal-tools

#### Usage
```[bash]
$ python run.py --help
usage: run.py [-h] [--project_name PROJECT_NAME] [--empty_project {0,1}]
              [--update_submodule UPDATE_SUBMODULE]

Internal tools

optional arguments:
  -h, --help            show this help message and exit
  --project_name PROJECT_NAME
                        Enter project name
  --empty_project {0,1}
                        Create empty project structure, ({0} - conan CMake app
                        structure), ({1} - conan CMake lib structure)
  --update_submodule UPDATE_SUBMODULE
                        update all submodule.
```

**To create CMake conan application structure [python script]**
```[bash] 
python run.py --project_name=sampleApplication --empty_project=0
```

**To create CMake conan library structure [python script]**
```[bash]
python run.py --project_name=sampleLibrary --empty_project=1
```

**Update submodule [python script]**
```[bash]
python run.py --project_name=sampleLibrary --empty_project=1
```

## other scripts
**Create linux conan enviroment [bash script]**
```[bash]
bash ./create_conan_linux_env 
```

