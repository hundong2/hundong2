How to use python module , the principle of pip
======
- set of *.py is *module* of python.
- for example, You type 'import numpy' or 'import pandas' to use numpy or pandas.
- This is what I call a file called numpy.py and a file called pandas.py that is stored on my computer.
- *When you install a new module, you use the command pip.*
- The important thing here is that the module you want to use must exist in my Python library.(In general, modules downloaded through pip are automatically saved to the Python library, but you need to remember that in some cases, you may download them by specifying a file path) 
- In other words, you cannot import a module after saving it on the desktop.

# pip command example

## install package 
```bash
pip install [package name]
```

## Show installed package list
```bash
pip list
```

## Find a specific installed package
```bash
pip show [pakage name]
```

## installed package upgrade 
```bash
pip install --upgrade [pakage name]
```

## remove installed package 
```bash
pip uninstall [package name]
```