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
        if "{{cookiecutter.dataset}}" == "Both":
            pass #We keep both
        elif "{{cookiecutter.dataset}}"=="Original dataset":
            remove("data/raw/DataDescriptionOpenSourced.md")
        elif "{{cookiecutter.dataset}}"=="Open sourced public dataset":
            remove("data/raw/DataDescriptionOriginal.md")
    def remove_pre_commit(self):
        if "{{cookiecutter.use_pre_commit}}"!="yes":
            remove(".pre-commit-config.yaml")










class CleanFilesPython3(CleanFiles):
    def __init__(self):
        super().__init__()
        self.docker_base_mapping={"python3.6":"python:3.6.12-buster","python3.7":"python3.7.9-buster","python3.8":"python3.8.6-buster","python3.9":"python3.9.0-buster"}

    def clean_tensorflow_files(self):
        pass

    def clean_pytorch_files(self):
        pass
    def write_read_me_file(self):
        import sys
        with open("Readme.md","r") as f:
            content=[]
            for line in f.readlines():
                content.append(line)
                if "Configuration instructions" in line:
                    content.append("Used python version is: {}.{}.{}\n".format(sys.version_info.major,sys.version_info.minor,sys.version_info.micro))

            f.close()
        with open("Readme.md","w") as f:
            for line in content:
                f.write(line)
            f.close()
    def modify_dockerfile(self):
        with open("Dockerfile",'r') as f:
            lines=f.readlines()

        lines[0]="FROM "+self.docker_base_mapping["{{cookiecutter.python_version}}"]
        with open("Dockerfile","w") as f:
            f.writelines(lines)









if "{{cookiecutter.language}}" == "python3" or "{{cookiecutter.language}}" == "python2.7":
    pass

if "{{cookiecutter.language}}" == "python3":
    cleanfile = CleanFilesPython3()
    cleanfile.remove_redundant_docker_files()
    cleanfile.remove_data_readme()
    cleanfile.remove_redundant_licenses()
    cleanfile.write_read_me_file()
    cleanfile.modify_dockerfile()
     # Then create a python3 project template
    if "{{cookiecutter.framework_if_using_python}}" == "pytorch":
        pass  # Use the pytorch
    elif "{{cookiecutter.framework_if_using_python}}" == "tensorflow":
        pass  # Do
    else:
        pass
elif "{{cookiecutter.language}}" == "python2.7":
    if "{{cookiecutter.framework_if_using_python}}" == "pytorch":
        pass
    elif "{{cookiecutter.framework_if_using_python}}" == "tensorflow":
        pass  # Do
    else:
        pass
elif "{{cookiecutter.language}}" == "R":
    pass
elif "{{cookiecutter.language}}" == "c++":
    pass
