# Python - data analysis course

## Prerequisites

- `git clone https://github.com/OliverZott/Python-Data-Science.git`

### Setup conda environment

- `conda env create -f datascience_env.yml` inside the repo
- `conda activate data_science` to activate env (also has to be done in VS Code!)
  - Check if Editor/Ide/Jupyter uses correct env and python-interpreter
  - `conda list` to check packages
- Maybe need to integrate conda-env into jupyter notebook/lab
  - <https://stackoverflow.com/questions/40694528/how-to-know-which-python-is-running-in-jupyter-notebook>
  - <https://stackoverflow.com/questions/53004311/how-to-add-conda-environment-to-jupyter-lab>

### Setup pip environment

- `python -m venv venv` ...environment

Environment activation/deactivation (windows/linux)

- `.\venv\Scripts\activate` or
- `activate`
- `. venv/bin/activate`
- `.\venv\Scripts\activate`
- `deactivate` or
- `deactivate env-name` or
- `.\venv\Scripts\deactivate`

Packages install:

- `pip list` to check current packages
- `python -m pip install --upgrade pip`
- `pip install -r requirements.txt --upgrade` or
- `pip install pandas numpy jupyterlab matplotlib seaborn autopep8 openpyxl plotly cufflinks`

Packages upgrade:

- `pip list --outdated`
- `pip freeze > pip_list.txt`   ...to freeze current state OR just use requirements-file.
- `pip install --upgrade --force-reinstall -r requirements.txt` ...to upgrade all packages

## Run

- Inside repo: `jupyter lab` or `jupyter notebook`

## Remarks

- **map**, **apply** [Link](https://stackoverflow.com/questions/19798153/difference-between-map-applymap-and-apply-methods-in-pandas)
- **loc** instead chained indexing [Link](https://stackoverflow.com/questions/13842088/set-value-for-particular-cell-in-pandas-dataframe-using-index)
- *List Comprehension* [Link](https://www.w3schools.com/python/python_lists_comprehension.asp)

- Selection in dataframes
  - <https://stackoverflow.com/questions/17071871/how-do-i-select-rows-from-a-dataframe-based-on-column-values>

### Time Series

- <https://www.dataquest.io/blog/tutorial-time-series-analysis-with-pandas/>
- <https://ichi.pro/de/zeitreihenanalyse-mit-pandas-in-python-271746212730840>
- <https://www.machinelearningplus.com/time-series/time-series-analysis-python/>
-
