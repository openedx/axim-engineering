# Code Examples

## Setup
To run the code examples, first install the prerequisites in a virtual environment.

    make requirements


## Examples

### isort
To run the isort example:
    
    isort isort_example/isort_example.py

To see the changes made:
    
    git diff isort_example/isort_example.py

### pylint
To run the pylint example:
    
    pylint pylint_example.py

### pycodestyle
To run the pycodestyle example:
    
    pycodestlye pycodestlye_example.py

### black
To run the black example:
    
    black black_example.py

To see the changes made:
    
    git diff black_example.py

### mypy
To see the mypy example, open `mypy_example.py` in any editor.

### pytest
To run the pytest example:
    
    pytest pytest_example.py

### coverage
To run the coverage example:
    
    coverage run coverage_example/test_example.py

To see the coverage report:
    
    coverage report -m

### sphinx
To build the sphinx example:
    
    cd docs && make html

To view the sphinx-rendered html page open `build/html/index.html' in any internet browser.
