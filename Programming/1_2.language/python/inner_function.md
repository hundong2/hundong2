# inner function of python

## List 

- [Zip()](#zip)
    - [Dictionary Zip()](#dictionary-zip)

## zip()

- 여러개의 순회 가능한 iterable 객체를 인자로 받아, 원소를 튜플 형태로 접근할 수 있는 반복자(iterator)를 반환합니다. 

 ### example 

```python
number = [1,2,3]
letters = ['a','b','c']

for _ in zip(number, letters):
    print(_)
```

 ### result 

```python
(1,'a')
(2,'b')
(3,'c')
```

### other example

#### dictionary zip

```python
dic(zip(["y","m","d"], [2022,3,13]))
```

##### result 
```python
{'y':2022,'m':3,'d':13}
```
