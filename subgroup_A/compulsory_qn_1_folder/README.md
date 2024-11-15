## COMPULSORY QUESTION 1

### Files and Notebooks
- `DSA3101_(A)Q1.ipynb`: A Jupyter Notebook that contains the analysis and findings for Question 1. This notebook includes data processing, visualization, and insights derived from customer experience data.
- `DockerFile`: A Docker configuration file to set up the environment for the project, ensuring consistent dependencies and configurations.
- `Survey_cleaned_balanced.xlsx`: The cleaned and balanced dataset used for analysis. This dataset contains information on visitor demographics, satisfaction scores, and spending behaviors.
- `dsa3101_(a)q1.py`: A Python script for the analysis of Question 1, similar to the Jupyter Notebook but designed for batch processing or command-line execution.
- `key_drivers.ipynb`: A Jupyter Notebook focused on identifying the key drivers of guest satisfaction and dissatisfaction. This analysis helps in understanding the factors that most influence visitor experience.
- `key_drivers.py`: A script version of the key_drivers.ipynb notebook. It includes functions to analyze satisfaction and dissatisfaction factors, which can be used in automated pipelines.
- `requirements.txt`: Lists all the dependencies required to run the project.

### Clone the Repository:
```
git clone https://github.com/tristontan/StatSmith.git

cd StatSmith/subgroup_A/compulsory_qn_1_folder # navigate to project directory
```
### Set up environment
```
docker build -t statsmith .
docker run -it statsmith
```
```
#alternatively, you could install the dependencies with

pip install -r requirements.txt
```
### USAGE

```
# execution of .py script

python dsa3101_(a)_q1_.py
```

