# HackerRank & Python Practice Programs (Formatted Version)

---

## 1. Solve Me First

https://www.hackerrank.com/challenges/solve-me-first/problem

```python
# Solve me first

def solveMeFirst(a, b):
    # Hint: Type return a+b below
    return a + b

num1 = int(input())
num2 = int(input())

res = solveMeFirst(num1, num2)
print(res)
```

**Output**

```
2
3
Expected Output
5
```

---

## 2. Simple Array Sum

https://www.hackerrank.com/challenges/simple-array-sum/problem

```python
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'simpleArraySum' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.

def simpleArraySum(ar):
    # Write your code here
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')
    fptr.close()
```

---

## Function for Finding Maximum and Minimum

```python
def maxmin(ar):
    b = 0
    c = ar[1]

    for i in ar:
        if i > b:
            b = i
        if i < c:
            c = i

    print("largest ", b)
    print("smallest ", c)

n = int(input("Enter range: "))
ar = []

for i in range(0, n):
    b = int(input("Enter digit: "))
    ar.append(b)

maxmin(ar)
```

---

## Types of Taking Input

```python
1. n = int(input(""))
2. a = int(input(""))
   b = int(input(""))
3. a, b = map(int(input("").split())
4. ls = list(map(int(input("").split()))
5. arr = eval(input())
```

---

## Remove Duplicate

```python
def remove(ar):
    ls = []
    for i in ar:
        if i not in ls:
            ls.append(i)
    return(ls)

n = int(input("Enter range: "))
ar = []

for i in range(0, n):
    b = int(input("Enter digit: "))
    ar.append(b)

print(remove(ar))
```

---

## Pattern

```python
i = 1
j = 10

while i < j:
    if i == 3 and j == 8:
        i = i + 1
        j = j - 1
        continue

    print(i, "\t", j)
    i = i + 1
    j = j - 1
```

**Output**

```
1     10
2     9
4     7
5     6
```

---

## Alternating Positive and Negative Numbers in an Array

```python
arr = [1, -2, 3, -4, -1, 4]

pos = []
neg = []

# separate positive and negative numbers
for i in arr:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)

result = []
i = j = 0

# arrange alternately
while i < len(pos) and j < len(neg):
    result.append(pos[i])
    result.append(neg[j])
    i += 1
    j += 1

# # add remaining elements
# result.extend(pos[i:])
# result.extend(neg[j:])

# print(result)
```
