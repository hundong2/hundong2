# Dictionary 

# Index 

[01.Duplicate Keys in .Net](#01-duplicate-keys-in-net)  

# Contents

## 01. Duplicate Keys in .Net

### 1.1 question 

- Duplicate keys in .NET dictionaries?  

### 1.2 Answers 

```c#
public class ListWithDuplicates : List<KeyValuePair<string, string>>
{
    public void Add(string key, string value)
    {
        var element = new KeyValuePair<string, string>(key, value);
        this.Add(element);
    }
}

var list = new ListWithDuplicates();
list.Add("k1", "v1");
list.Add("k1", "v2");
list.Add("k1", "v3");

foreach(var item in list)
{
    string x = string.format("{0}={1}, ", item.Key, item.Value);
}
```

### 1.3 reference 

[stackoverflow question](https://stackoverflow.com/questions/146204/duplicate-keys-in-net-dictionaries)  

