# JAVA
## hash
### getOrDefault function
<p>
A method that returns the value of the searched key if the searched key exists, and returns the default value if it does not exist.
</P>

### function 
```java
getOrDefault(Object key, V DefaultValue)
```

This method accepts two parameters.

<p>
key : The key of the element from which the value should be retrieved.

defaultValue : The default value that should be returned if there is no value mapped to the specified key.

Return value: If the key to be searched exists, the value mapped to the key is returned, otherwise the default value is returned.
</p>

### Program 1
```java
// Java program to demonstrate
// getOrDefault(Object key, V defaultValue) method
  
import java.util.*;
  
public class GFG {
  
    // Main method
    public static void main(String[] args)
    {
  
        // Create a HashMap and add some values
        HashMap<String, Integer> map
            = new HashMap<>();
        map.put("a", 100);
        map.put("b", 200);
        map.put("c", 300);
        map.put("d", 400);
  
        // print map details
        System.out.println("HashMap: "
                           + map.toString());
  
        // provide key whose value has to be obtained
        // and default value for the key. Store the
        // return value in k
        int k = map.getOrDefault("b", 500);
  
        // print the value of k returned by
        // getOrDefault(Object key, V defaultValue) method
        System.out.println("Returned Value: " + k);
    }
}
```

#### Output

```
HashMap: {a=100, b=200, c=300, d=400}
Returned Value: 200
```

### Program2
```java
// Java program to demonstrate
// getOrDefault(Object key, V defaultValue) method

import java.util.*;

public class GFG {

	// Main method
	public static void main(String[] args)
	{

		// Create a HashMap and add some values
		HashMap<String, Integer> map
			= new HashMap<>();
		map.put("a", 100);
		map.put("b", 200);
		map.put("c", 300);
		map.put("d", 400);

		// print map details
		System.out.println("HashMap: "
						+ map.toString());

		// provide key whose value has to be obtained
		// and default value for the key. Store the
		// return value in k
		int k = map.getOrDefault("y", 500);

		// print the value of k returned by
		// getOrDefault(Object key, V defaultValue) method
		System.out.println("Returned Value: " + k);
	}
}
```

#### Output
```
HashMap: {a=100, b=200, c=300, d=400}
Returned Value: 500
```

Reference
======
[hashmap](https://docs.oracle.com/javase/8/docs/api/java/util/HashMap.html#getOrDefault-java.lang.Object-V- "java")

[geeksforgeeks](https://www.geeksforgeeks.org/hashmap-getordefaultkey-defaultvalue-method-in-java-with-examples/ "geeksforgeeks")