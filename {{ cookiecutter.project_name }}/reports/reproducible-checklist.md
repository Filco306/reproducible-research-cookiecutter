# Reproduction of results, checklist

This code is reproducible, because of the reasons below. If you wonder why these checklists, motivations can be found in `design/FAQ.md`.

- [ ] It contains a Dockerfile that will automatically reproduce the experiments in the repository.
  - [ ] If GPU:s were used, a Dockerfile that leverages these exist.
  - [ ] The Dockerfile does not have a `:latest`-tag on the `FROM`-lines.
- [ ] Seed for randomizations of the initial experiments are used throughout the project and are documented in `RANDOM_SEEDS.md`.
- [ ] Links to the open data sources are referenced in the `README.md`.

{%- if cookiecutter.language=="python3" or cookiecutter.language=="python2.7" -%}
## Python checklist
- [ ] All packages used for the project are listed in a `requirements.txt` with all packages in the format `PACKAGE_NAME==VERSION_USED`. If the project uses a package that is not pip-installable, an instruction on how to install it to reproduce results is attached.
- [ ] The use of linters such as [flake8](https://github.com/PyCQA/flake8) and [black](https://github.com/psf/black) is implemented.
{%- elif cookiecutter.language == "R" -%}
## R checklist
{%- elif cookiecutter.language == "c++" -%}
## C++ checklist
- [ ] If the project is made in C++, the use of linters such as [cpplint](https://github.com/cpplint/cpplint)
{%- endif -%}
## Additional quality-raising features
- [ ] A paper is referenced in the `README.md`, included in the `reports/`-folder or a `reports/METHODOLOGY.md` is attached in the repository.
- [ ] Tests are included in the repository to test the most essential features of the experiments to quickly see that things work.
- [ ] A link to a container registry to a Docker container in which the original experiments were performed is listed in the `README.md`.
- [ ] When code is copied from other repositories or sources, these are referenced (__even sources such as StackOverflow__).
- [ ] The code adheres to coding standards.
- [ ] The code is well documented using a tool such as `mkdocs` or `pdocs`.
- [ ] I have added a .env.example-file which lists all environment variables needed for this project.