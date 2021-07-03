"""
with the help of this script, create CMake supported conan template empty structure.
"""
import argparse
import shutil
import json
import os

def replace_test_in_file(file, from_text, to_text):
    with open(file) as f:
        newText = f.read().replace(from_text, to_text)
    with open(file, "w") as f:
        f.write(newText)

def create_structure(config_file, project_name, option_type):
    with open(config_file) as file:
        data = json.load(file)
    dest = 'out/'+project_name+'/'
    if os.path.exists('out'):
        shutil.rmtree('out')
    os.makedirs(dest)
    for d in data["folder"]:
        dir_d = dest+d["target"]+d["name"]
        print('created folder: ', dir_d)
        if not os.path.isdir(dir_d):
            os.makedirs(dir_d+"/")
    for d in data['file']:
        print('created file: ', dest+d["target"]+d["name"])
        here = os.path.dirname(os.path.abspath(__file__))
        shutil.copy2(os.path.join(here,d["path"]), dest+d["target"])
    for d in data['file']:
        d2 = dest+d["target"]+d["name"]
        if d["name"] == "CMakeLists.txt" or d["name"] == "README.md":
            replace_test_in_file(d2, "example", project_name)
        if option_type == 1:
            if d["name"] == "CMakeLists.txt":
                replace_test_in_file(d2, "exampleApp", project_name+"App")
                replace_test_in_file(d2, "exampleLib", project_name+"Lib")
                replace_test_in_file(d2, "exampleTest", project_name+"Test")
            elif d["name"] == "conanfile.py":
                replace_test_in_file(d2, "exampleLib", project_name+"Lib")
                replace_test_in_file(d2, "exampleConan", project_name+"Conan")

def empty_project_argument(empty_project, project_name):
    option_type = empty_project
    config_file = ""

    here = os.path.dirname(os.path.abspath(__file__))
    if option_type == 0:
        config_file = os.path.join(here,'configuration/conan_application.json')
    elif option_type == 1:
        config_file = os.path.join(here,'configuration/conan_library.json')

    create_structure(config_file, project_name, option_type)
    print('Done, please check \"out\" folder.')

def main():
    if os.path.isdir('out'):
        shutil.rmtree('out')
    parser = argparse.ArgumentParser(description='Template-creator')
    parser.add_argument("--name", type=str, help="Enter project name")
    parser.add_argument("--ptype", type=int, choices=[0, 1],
                        help="Create empty project structure, ({0} - conan CMake app structure), ({1} - conan CMake lib structure)")
    
    args = parser.parse_args()

    if args.name is not None and args.ptype is not None:
        empty_project_argument(args.ptype, args.name)