# insights

## Setting up a development environment

1. Create a virtual environment for Python
    1. Using pip: `pip install -r requirements/development.txt`
    2. Using conda: `conda env create -f environment.yaml`
2. Install the pre-commit hooks with `pre-commit install`

## Running the code quality analysis tools

* Run `tox`.

### Running only the linters step

* Run `tox -e lint` to lint the source code.

### Running only the tests step

* Run `tox -e test` to execute all tests.

### Running only the documentation build step

* Run `tox -e documentation` to build the documentation files.
