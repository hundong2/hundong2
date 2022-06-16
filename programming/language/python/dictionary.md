# Dictionary(딕셔너리)
## dictionary
- immutable key & mutable value로 mapping이 되어 있는 순서가 없는 집합. 

```python
>>> { "test":1, "test2":2}
{'test': 1, 'test2': 2}
```

- Key는 immutable 사용가능, but, mutable한 객체는 사용 불가. 

### immutable example
```python
>>> test = { 1:5, 2:3} #int using 
>>> test
{1: 5, 2: 3}
>>> test = { (2,4):1, (4,3):4} #tuple using
>>> test
{(2, 4): 1, (4, 3): 4}
>>> test = {2.4:2,"dmf":4} #float using
>>> test
{2.4: 2, 'dmf': 4}
>>> test = { True:2,"dmf":5} #bool using
>>> test
{True: 2, 'dmf': 5}
```

### mutable example
```python
>>> test = {{1,4}:1, {3,5}:5}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'

>>> test = {[1,3]:2,[4,3]:4}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'

>>> test = { {"test2":3}:2, "dfd":4}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'
```

### tip 1
- value overlap possible, 
- but, key is overwirted ( last data )

```python
>>> {"test":2, "test":4}
{'test': 4}
```

### tip 2
- Because there is no order, 
- it cannot be accessed by index, but by key.
```python
>>> help = {"112":112,"119":119}
>>> help[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0

>>> help["112"]
112
```

### tip3
- Since it is a mutable object, the value can be changed by accessing it with a key.
```python
>>> help["112"] = 114
>>> help["112"]
114
```

### tip4
- You can add new keys and values ​​like below.
```python
>>> help["114"] = 114
>>> help
{'112': 114, '119': 119, '114': 114}
```





