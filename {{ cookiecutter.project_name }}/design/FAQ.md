# Why do all these things? An FAQ

## Why should I use Docker?

A Docker image enables everyone with Docker installed to use your code and avoid complications with differences in OS:es, package version and the like.

## Why should my Docker image not have the :latest tag?

Having the `:latest`-tag means that you will pull down the latest version of the image from which you are building, meaning there will be differences in the technology you pull down a time later once a new version of the image you used has been released. This changes the circumstances under which your experiments were performed, and therefore possibly the results.

## Why should I have links to the data I used for my experiments?

In order to reproduce the results, one needs to use the same data that you have used.

## Why should I document the seeds I have used for my code?

Seeds determine the random state of the program. If you use any type of randomization in your code, these seeds will have an impact on the outcome. Therefore, it is important to set all these and ensure that they are documented.

## Why should I have a requirements.txt if my project is implemented in python?

A `requirements.txt`-file has the same purpose as not using the `:latest`-tag. It will ensure that anyone who tries to reproduce your results will have the same versions of all your python-packages that you used at the time of reproduction.


# Why tick off the quality-enhancing features?

## Why adhere to coding standards using tools such as linters?

Using linters and code cleaners improve the readability and reduces the risk of bugs and side-effects in your code.
