# Reproduction of results, checklist

This code is reproducible, because of the reasons below.

- [ ] It contains a Dockerfile that will automatically reproduce the experiments in the repository.
  - [ ] If GPU:s were used, a Dockerfile that leverages these exist.
  - [ ] The Dockerfile does not have `:latest`-tags, since these.
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
- [ ] My code is well documented.

## Why do all these things? An FAQ

### Why should I use Docker?

A Docker image enables everyone with Docker installed to use your code and avoid complications with differences in OS:es, package version and the like.

#### Why should my Docker image not have the :latest tag?

Having the `:latest`-tag means that you will pull down the latest version of the image from which you are building, meaning there will be differences in the technology you pull down a time later once a new version of the image you used has been released. This changes the circumstances under which your experiments were performed, and therefore possibly the results.

### Why should I have links to the data I used for my experiments?

In order to reproduce the results, one needs to use the same data that you have used.

### Why should I document the seeds I have used for my code?

Seeds determine the random state of the program. If you use any type of randomization in your code, these seeds will have an impact on the outcome. Therefore, it is important to set all these and ensure that they are documented.

### Why should I have a requirements.txt if my project is implemented in python?

A `requirements.txt`-file has the same purpose as not using the `:latest`-tag. It will ensure that anyone who tries to reproduce your results will have the same versions of all your python-packages that you used at the time of reproduction.


## Why tick off the quality-enhancing features?

### Why adhere to coding standards using tools such as linters?

Using linters and code cleaners improve the readability and reduces the risk of bugs and side-effects in your code. 
