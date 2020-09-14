#!/usr/bin/env python3
import os
import shutil


# COPIED FROM https://github.com/cookiecutter/cookiecutter/issues/723
def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if "{{cookiecutter.language}}" == "python3":
    pass  # Then create a python3 project template
    if "{{cookiecutter.framework}}" == "pytorch":
        pass  # Use the pytorch
    elif "{{cookiecutter.framework}}" == "tensorflow":
        pass  # Do
    else:
        pass
elif "{{cookiecutter.language}}" == "python2.7":
    if "{{cookiecutter.framework}}" == "pytorch":
        pass
    elif "{{cookiecutter.framework}}" == "tensorflow":
        pass  # Do
    else:
        pass
elif "{{cookiecutter.language}}" == "R":
    pass
elif "{{cookiecutter.language}}" == "c++":
    pass
