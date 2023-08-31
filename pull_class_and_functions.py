import sys
import os
from inspect import isfunction, isclass
import pprint

# change path
FILE_PATH = "add_your_path"

path = os.path.abspath(FILE_PATH)
sys.path.append(path)

# change file name
import <file_name> as file

pp = pprint.PrettyPrinter(indent=4)

def main():
    classes = [thing for thing in dir(file) if isclass(getattr(file, thing))]
    functions = [thing for thing in dir(file) if isfunction(getattr(file, thing))]

    all_class_methods = {}
    for item in classes:
        all_class_methods[item] = []
        inspecting = getattr(file, item)
        for attr in dir(inspecting):
            if not attr.startswith("__") and not attr.startswith("_"):
                method = getattr(inspecting, attr)
                if isfunction(method):
                    all_class_methods[item].append(attr)

    print('All functions: ')
    pp.pprint(functions)
    print()
    print('All classes and methods: ')
    pp.pprint(all_class_methods)

if __name__ == "__main__":
    main()