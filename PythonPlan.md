# Plans for reproducible python research project template in Data Science/Machine Learning
This file contains all the nessasary component we should have in the generated template in order to have a research project that is reproducible/easy to reproduce

## Data/Post Processing of the data
- A folder named "Data" in the root directory where the raw data should be placed
- If the used data is not permitted to be placed in the repo for some reason, this folder can be empty
- A markdown file "data_description.md" should be placed in the Data folder where it contains at least on of the following, user should be able to pick between either of them upon creating the project, by choosing "Some known dataset" or "New dataset or modified version of some existed dataset"
	- if using some well known/published open sourced dataset that everyone can have acesss to and download the exactly same dataset, a link to the referenced dataset/original paper should be enough.
	- if the research actually using its own datasets that was not avaliable to the public before (The dataset is published for the first time in this research project or the author is using a modified version of some existed dataset such as adding extra feature columns .etc), a full description of the dataset should be written in this file.


## Results
- A main foler called "Result" in the root directory
- Inside the "Result" folder there should be
	- "experimental_results" where the experimental result/trial&error results be placed, all the data here can be safely deleted/removed 
	- "checkpoint_results" where milestone results that the author wish to save for future usage are stored here, in each of the subdirectory in this foler a config file of hyper-parameters should be placed, hopefully a dockerimage can also be placed here for other user to reproduce the result.


## Requirement
- A requirement.txt in the root directory where one can use `pip install -r requirement.txt` directly

## Licence
- A LICENCE file in the root directory

## Examples/scripts for reproduce
- In this directory, some examples of the research work can be placed.
- Divided in sub-directories, each directory contains a docker image and bash scripts for reproduce

## Bash file for generating the docker images
- The user might want to create many different docker images for different models and different experiments throughout their research cycle, this batch file can be run to generate a docker image based on the current settings of the project, using the dockerfile in the root directory.

## Logs
- A directory under root directory, here 

## Version Control
- Add git and gitignore files in the directory for version control

## Tests
- Just add a folder maybe, or we can write some empty template for testing using pytest

## GPU support for docker
- If the user wish to use GPU in their project, we might need 2 versions of dockerfile, one supporting Nvidia container toolkit and one not.
- FROM nvidia/cuda:10.2-base\
CMD nvidia-smi\
at the begining of the dockerfile


## source codes
- a "src/" directory in the root directory

## Reminder for reproducibility factors that we cannot actually control
- Random state
- Hardware such as cpu architechture, gpu, cuda .etc
- Optimization




## utils
- Some very general utility modules are placed in src/utils, while these modolues are served as a wrapper/decorators to some other functions that add some extra benefits that everyone likes
	- __init__.py ofc
	- a decorator for training, exports trained model to the "Models" folder while saving all the hyper-parameters, used datasets, any other specifications such as experiment time/training time to "Logs/train"
	- a decorator for generating/result, just like the training case, this python module should be a decorator of a generate_result/perdict function and write logs to "Logs/result"
	- A command line parser maybe? I feel the authors might enjoy more to write their own main.py/run.py/.etc
