# Counter 
## Explanation
데이터의 개수를 셀 때 사용.
`collections` 모듈의 `counter` 

### Dictionary를 이용한 Counter 
```python
def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter

countLetters('hello world'))
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

### collections의 Counter 이용 시

파이썬에서 제공하는 `collections` 모듈의 `Counter` 클래스를 사용하면 위 코드를 단 한 줄로 줄일 수가 있습니다.

```python
from collections import Counter
Counter('hello world') # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```
collections.Counter 기본 사용법
collections 모듈의 Counter 클래스는 별도 패키지 설치 없이 파이썬만 설치되어 있다면 다음과 같이 임포트해서 바로 사용할 수 있습니다.
### collections.Counter 기본 사용법

`collections` 모듈의 `Counter` 클래스는 별도 패키지 설치 없이 파이썬만 
설치되어 있다면 다음과 같이 임포트해서 바로 사용할 수 있습니다.

```python
from collections import Counter
```

collections 모듈의 Counter 클래스는 파이썬의 기본 자료구조인 사전(dictionary)를 확장
사전에서 제공하는 API를 그대로 다시용할 수가 있습니다.

예를 들어, 주어진 단어에서 가장 많이 등장하는 알페벳과 그 알파벳의 개수를 구하는 함수는 
다음과 같이 마치 사전을 이용하듯이 작성할 수 있습니다.
```python
from collections import Counter

def find_max(word):
    counter = Counter(word)
    max_count = -1
    for letter in counter:
        if counter[letter] > max_count:
            max_count = counter[letter]
            max_letter = letter
    return max_letter, max_count

find_max('hello world') # ('l', 3)
```
[collections reference](https://github.com/python/cpython/blob/3.10/Lib/collections/__init__.py "collection")