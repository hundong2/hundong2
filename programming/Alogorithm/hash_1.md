# code 
`Problem category`
<p>
Athletes who did not finish

Problem Description
Many marathon runners took part in the marathon. All but one runner completed the marathon.

Write a solution function to return the names of the runners who did not finish when an array containing the names of the participants who participated in the marathon and an array containing the names of the runners who completed the marathon are given.

restrictions
The number of runners participating in the marathon is at least 1 and not more than 100,000.
The length of completion is 1 less than the length of the participant.
Participants' names must consist of at least 1 and no more than 20 lowercase letters of the alphabet.
Participants may have the same name.
</p>

## 입출력 예

|participant	                |completion             |return     |
|:---                           |:---                   |:---       |
|["leo", "kiki", "eden"]        |["eden", "kiki"]       |"leo"      |
|["marina", "josipa", "nikola", "vinko", "filipa"]|	["josipa", "filipa", "marina", "nikola"]	|"vinko"|
|["mislav", "stanko", "mislav", "ana"]| ["stanko", "ana", "mislav"]	| "mislav" |

## 입출력 예 설명
### 예제 #1
"leo" is on the roster of participants, but not on the runners list, so he didn't finish.

### 예제 #2
"vinko" was on the roster of participants, but not on the runners list, so she didn't finish.

### 예제 #3
"mislav" has two on the list of participants, but only one on the list of finishers, so one didn't finish.


## Problem solving 
# C++ 
```c++
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    for(int i=0;i<completion.size();i++)
    {
        if(participant[i] != completion[i])
            return participant[i];
    }
    return participant[participant.size() - 1];
    //return answer;
}
```

## JAVA (HASH)
```java
import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hm = new HashMap<>();
        for (String player : participant) hm.put(player, hm.getOrDefault(player, 0) + 1);
        for (String player : completion) hm.put(player, hm.get(player) - 1);

        for (String key : hm.keySet()) {
            if (hm.get(key) != 0){
                answer = key;
            }
        }
        return answer;
    }
}
```

## Python
```python
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
```

## javascript
```javascript
var solution=(_,$)=>_.find(_=>!$[_]--,$.map(_=>$[_]=($[_]|0)+1))
```
### same means 
```javascript
var solution=(participant,completion)=>participant.find(name=>!completion[name]--,completion.map(name=>completion[name]=(completion[name]|0)+1))
```

# Reference

[for_each](../language/c++/for_each.md)

[getOrDefault](../language/java/hash/getOrDefault.md)

[collection](https://docs.python.org/ko/3/library/collections.html "collection")

[collection/ini.py](https://github.com/python/cpython/blob/3.10/Lib/collections/__init__.py "collection_init")

[collection Counter](../language/python/collection/counter.md)

# Site 

[Programmers](https://programmers.co.kr/learn/courses/30/lessons/42576 "42576")

[COCI contest](https://hsin.hr/coci/archive/2014_2015/contest2_tasks.pdf "contest2_task")