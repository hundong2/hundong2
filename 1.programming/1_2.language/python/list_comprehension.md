# list comprehension

## example 

## if you don't use to list comrehension 

```python
>>> a = []
>>> for n in range(1, 10 + 1)
...     if n % 2 == 1:
...         a.append(n*2)
```

## use list comprehension

```python
[n*2 for n in range(1,10+1) if n % 2 == 1 ]
```

### result

```bash
[2, 6, 10, 14, 18]
```



