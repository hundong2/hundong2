# Python module ( imported ) location look up

```python
>>> import inspect
>>> print(inspect.getfile(random)) # imported element
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'random' is not defined
>>> import random #import random.py
>>> print(inspect.getfile(random))
C:\[UserFilePath]\Anaconda3\lib\random.py
```