# f-string 

## 1. string formatting 

- python version 3.6 UPPER 
- f'문자열~{변수}~문자열' 
- {변수}로 채워준 구문을 넣어주면 사용 가능. 

### exmaple 

```python
day = 1
while day <= 31:
    print(f'2021.06.{day}')
    day = day + 1
```

## 2. f-string arrangement ( left, center, right )

```python
py# f-string 왼쪽 정렬
s1 = 'left'
result1 = f'|{s1:<10}|'
print(result1) 

# f-string 가운데 정렬
s2 = 'mid'
result2 = f'|{s2:^10}|'
print(result2) 
# f-string 오른쪽 정렬
s3 = 'right'
result3 = f'|{s3:>10}|'print(result3)
print(result3)
```

### result 
```bash
|left      |
|   mid    |
|     right|
```


## 3. f-string { } 

```python
number = 123
result = f'my value {{{number}}} {{number}}'
print(result)
```

### result
```bash
my value {123} {number}
```
## 4. f-string and dictionary

```python
# f-string과 딕셔너리
d = {'name': 'BlockDMask', 'gender': 'man', 'age': 100}
result = f'my name {d["name"]}, gender {d["gender"]}, age {d["age"]}'
print(result)
```

### result
```bash
my name BlockDMask, gender man, age 100
```

## 5. f-string and list

```python
n = [100, 200, 300] 
print(f'list : {n[0]}, {n[1]}, {n[2]}')  
for v in n:    
    print(f'list with for : {v}')
```

### result 
```bash
list : 100, 200, 300
list with for : 100
list with for : 200
list with for : 300
```

## reference 

[개발자 지망생:티스토리]( https://blockdmask.tistory.com/429 )