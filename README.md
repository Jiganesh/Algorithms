### Boiler Plate

```
import math
from collections import deque, defaultdict, Counter

```





### Counter comparisions**


`Counter(A) <  Counter(B)` to be True

- Every element in A must have count <= its count in B 
AND
- At least one element in A must have count STRICTLY LESS than its count in B


`Counter(A) <=  Counter(B)` to be True

- Every element in A must have count <= its count in B 


`Counter(A) >  Counter(B)` to be True

- Every element in B must have count <= its count in A
AND
- At least one element in B must have count STRICTLY LESS than its count in A

---


### Math - Find Powers

Find if "n" is power of "m"


```   return  m ** int(math.log10(n) / math.log10(m)) == n ```

---

### Short-Circuting and Condition Evaluation

(5%2==0) and "EVEN" or "ODD"  -> will result in ODD 

- How is this statement resolved in python ?

Let's understand "and" and "or "resolution

- For and if any condition is False then the entire chain is False so it has to evaluate entire chain trying to find Falsy Value
- For or  if any condition is True then it will return True which is why it just needs to find first Truthy value

`(condition1) and (condition2) and (condition3)`
- Let's consider condition1 is True, After determining condition1 is True it will move forward in chain to check if any value is falsy
- Let's consider condition2 is False, After determining condition2 is False it will return False as not point in moving forward in chain.

`(condition1) or (condition2) or (condition3)`
- Let's consider condition1 is True, After determining condition1 is True it will return True as not point in moving forward in chain.
- Let's consider condition1 and condition2 is False, Hoping that condition3 can be True it will move and evaluate all conditions


**Let's take few examples <condition1> operator <condition2>**

True and "Jiganesh" => This evaluation has determined that condition1 is True so python will process next condition "Jiganesh", as python is evaluating condition2 it does not matter if it is True or False it will return this value.

False and "Jiganesh" => This evaluation has determined that condition1 is False so python will return False as it will not be moving forward in chain 

True or "Jiganesh" => This evaluation has determined that condition1 is True so python will return True as it will not be moving forward in chain

False or "Jiganesh" => This evaluation has determined that condition1 is False so python will process next condition "Jiganesh", as python is evaluating condition2 it does not matter if it is True or False it will return this value.


Coming back to our example (5%2==0) and "EVEN" or "ODD"  -> will result in ODD 


(5%2==0) is False
False and "EVEN" will return False (short-circuted)
False or "ODD" will return ODD

Hence the result of (5%2==0) and "EVEN" or "ODD" will be "ODD"