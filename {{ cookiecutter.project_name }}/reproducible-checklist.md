# Reproduction of results, checklist

This code is reproducible, because of the reasons below. If you wonder why these checklists, motivations can be found in `design/FAQ.md`.

- [ ] It contains a Dockerfile that will automatically reproduce the experiments in the repository.
  - [ ] If GPU:s were used, a Dockerfile that leverages these exist.
  - [ ] The Dockerfile does not have a `:latest`-tag on the `FROM`-lines.
- [ ] Seed for randomizations of the initial experiments are used throughout the project and are documented in `RANDOM_SEEDS.md`.
- [ ] Links to the open data sources are referenced in the `README.md`.
- [ ] If the project is mainly written in python, all packages used for the project are listed in a `requirements.txt` with all packages in the format `PACKAGE_NAME==VERSION_USED`. If the project uses a package that is not pip-installable, an instruction on how to install it to reproduce results is attached.


## Additional quality-raising features
- [ ] A paper is referenced in the `README.md`, or a `METHODOLOGY.md` is attached in the repository.
- [ ] A link to a container registry to a Docker container in which the original experiments were performed is listed in the `README.md`.
- [ ] When code is copied from other repositories or sources, these are referenced (__even sources such as StackOverflow__).
- [ ] The code adheres to coding standards.
    - [ ] If the project is made in python, the use of linters such as [flake8](https://github.com/PyCQA/flake8) and [black](https://github.com/psf/black) is implemented.
    - [ ] If the project is made in C++, the use of linters such as [cpplint](https://github.com/cpplint/cpplint)
- [ ] The code is well documented using a tool such as `mkdocs` or `pdocs`.
