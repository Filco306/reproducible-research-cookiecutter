#!/usr/bin/env python3
import os
import shutil

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


class CleanFiles:
    def __init__(self):
        pass

    def remove_redundant_docker_files(self):
        remove("Dockerfiles")

    def remove_redundant_licenses(self):
        remove("licenses")

    def remove_data_readme(self):
        if "{{cookiecutter.dataset}}"=="Original dataset":
            remove("data/raw/DataDescriptionOpenSourced.md")
        elif "{{cookiecutter.dataset}}"=="Open sourced public dataset":
            remove("data/raw/DataDescriptionOriginal.md")


class CleanFilesPython3(CleanFiles):
    def __init__(self):
        super().__init__()

    def clean_tensorflow_files(self):
        pass

    def clean_pytorch_files(self):
        pass








cleanfile=CleanFilesPython3
cleanfile.remove_redundant_docker_files()
cleanfile.remove_data_readme()
cleanfile.remove_redundant_licenses()
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
