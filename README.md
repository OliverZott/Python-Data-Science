# Setup

`git clone https://github.com/OliverZott/Python-Data-Science.git`

## Setup conda environment

- `conda env create -f datascience_env.yml` inside the repo
- `conda activate data_science` to activate env (also has to be done in VS Code!)
    - Check if Editor/Ide/Jupyter uses correct env and python-interpreter
    - `conda list` to check packages
- Maybe need to integrate conda-env into jupyter notebook/lab
    - https://stackoverflow.com/questions/40694528/how-to-know-which-python-is-running-in-jupyter-notebook
    - https://stackoverflow.com/questions/53004311/how-to-add-conda-environment-to-jupyter-lab

## Setup pip environment

- `python -m venv venv`

### Activate

- windows:
    - `.\venv\Scripts\activate` or
    - `activate`
- linux:
    - `. venv/bin/activate`
    - `.\venv\Scripts\activate`

### Deactivate~~~~

- `deactivate` or
- `deactivate env-name` or
- `.\venv\Scripts\deactivate`

### Install packages

- check first
    - `pip list`
    - `python -m pip install --upgrade pip`

- install packages
    - `pip install -r requirements.txt --upgrade` or
    - `pip install pandas numpy jupyterlab matplotlib seaborn autopep8 openpyxl plotly cufflinks`

# Additional Resources

### Time Series

- https://www.dataquest.io/blog/tutorial-time-series-analysis-with-pandas/
- https://ichi.pro/de/zeitreihenanalyse-mit-pandas-in-python-271746212730840
- https://www.machinelearningplus.com/time-series/time-series-analysis-python/
- 
