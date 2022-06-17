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
W
## installed package upgrade 
```bash
pip install --upgrade [pakage name]
```

## remove installed package 
```bash
pip uninstall [package name]
```
## Check current python library path 
```bash
>>> import sys
>>> sys.path
```

## Add python pacakge ( semi-permanent )
```bash
import sys
sys.path.append("[add path]") #add path
sys.path #confirm path
```
## Add python pacakge ( everasting )

### Window
- In the folder where python is installed, open site-packages in the Lib folder, create [file name].pth in the folder, and write the path to be added.

### Linux/mac
```bash
export PYTHONPATH="${PYTHONPATH}:[path name]"
```