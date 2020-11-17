#Plan of the Reproducible research code project
##What I did
###Installed cookiecutter, created one research project using the latest template
###Read cookiecutter documentation and presentation videos on web.
###Tested some famous cookiecutter projects, e.g. audreyfeldroy/cookiecutter-pypackage
###Read programming best practices for python, Java, R

##What makes research code non-reproducible?
### Data cannot be fully accessed by other researchers/Lacks description or code of postprocessing of the data
It is obvious that the result becomes ireproducible when the data is not fully accessble. But there are more situations.\
For example, how is traning set and test set been divided. What kind of postprocessing does one need to perform before running the code. \
Some research work only provides link/reference to the original data resource/some public datasets, but using some postprocessed data.\

###Decision of hyper-parameters/model details not documented
Hyper-parameters such as training rate, drop out rate, etc are essential for reproducing the results.
###No specified computing infrastructure used for running experiments (hardware and software), including GPU/CPU models; amount of memory; operating system; names and versions of relevant software libraries and frameworks.
###Number of experiments/measures of performance/measures of uncertainty are not specified
Many algorithm/model are highly volatile and can give different results for different runs. One need to know these things for reprocucing the complete result.
### Random state not provided
If the algorithm involves randomness or data partition relies on randomness, how the random state/random seed are decided are needed.
### Lack of version-control of the code
Even the slightest change to a computer program can have large intended or unintended consequences. When a continually developed piece of code (typically a small script) has been used to generate a certain result, only that exact state of the script may be able to produce that exact output, even given the same input data and parameters.


##How do we solve them?

1. One should write documentation of postprocessing of the raw data/provide code for postprocessing the data
2. Raw data should always be placed in Data folder, where the results/plots are placed in a separate folder. We do not want the files generated during the execution pollutes the Data folder.
3. A document discribes the decision of hyper-parameters. If different hyper-parameters are used for different experiments/use cases, it should be placed in this document.
4. Create a Docker image to avoid computing infrastracture problems. However, using a GPU could be problematic. Docker container does not support GPU natively, we might need some tool like Nvidia Container Toolkit. But it still requires the original machine installs the correct Nvidia driver. We might want the author provide both gpu/cpu version of the code.
5. A Batch file that one can run from commandline that generates the result we want to reproduce.
6. A batch file that generates the desired Dokcer image file?
7. Should we go for a PyPi approach or docker approach?
8. Version control


##What makes reproducible research code not usable in practice?

### Code with little/no comments
### Code that lacks modularity, all the code hangs together
### Bad programming habits that don't follow programming best practices.
### Bad optimization
The result might be reproducible, but training/execution could take forever due to bad optimization. For example uncesscerry repeated copy in loops, calling the same function on the same value without saving the result. etc

##How do we improve them?
1. Use linter for different languages. User should be able to decide yer/no upon initialization of the project.
2. Some dafult modules with function templates.
3. Optimization reminder document maybe? I dont know if there is a better way other than the effort by the authors.


##Some good habit
### Write an experiemnt log that records what experiemnts have been done so far
Whenever a result may be of potential interest, keep track of how it was produced. 
### Always store raw data, not only plots, including hyper-parameters
It could be fruitful if we could have a folder that stores all the raw result data and hyper_parameters. We could do this by writing a wrapper of the executable and place the raw output and input tags to this folder with appropreate sub-directories.


https://github.com/lancopku/AMM
https://github.com/studio-ousia/luke
https://github.com/freesunshine0316/neural-graph-to-seq-mp

