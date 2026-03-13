# Algorithms and Data Structures – Basic Concepts

## 1. Algorithm

An **algorithm** is a step-by-step set of instructions used to solve a problem or perform a computation in a program.

Example:
Steps to reverse a number:

1. Take input from the user
2. Extract the last digit
3. Add it to the reversed number
4. Remove the last digit from the original number
5. Repeat until the number becomes zero

---

# 2. Data Structures

A **Data Structure** is a way of organizing and storing data so it can be accessed and modified efficiently.

## Types of Data Structures

### 1. Primitive Data Structures

These are basic built-in data types.

Examples:

* Integer
* Float
* Character
* String
* Boolean

### 2. Non-Primitive Data Structures

#### Linear Data Structures

Data elements are arranged sequentially.

Examples:

* Arrays
* Linked Lists
* Stacks
* Queues

Example structure:

A → B → C → D

#### Non-Linear Data Structures

Data elements are connected hierarchically or as networks.

Examples:

* Trees
* Graphs

Example structure:

```
      A
     / \
    B   C
   / \
  D   E
```

---

# 3. Big O Notation

**Big O Notation** is used to measure the efficiency of an algorithm as the input size increases.

It describes how the running time or memory usage grows.

Example:

| Input Size | Runtime     |
| ---------- | ----------- |
| 10         | Fast        |
| 1000       | Slower      |
| 1,000,000  | Much slower |

---

# 4. Time and Space Complexity

## Time Complexity

Measures how long an algorithm takes to run.

Example:
Program A = 30 seconds
Program B = 60 seconds

Program A is more efficient.

## Space Complexity

Measures how much memory an algorithm uses.

---

# 5. Performance Cases

Algorithms are analyzed in three cases.

### Best Case

Minimum time required.

### Average Case

Normal expected performance.

### Worst Case

Maximum time required.

---

# 6. Types of Complexity Notations

## Big O (O)

Represents the **upper bound (worst case)**.

Example:
O(n)

## Big Omega (Ω)

Represents the **lower bound (best case)**.

Example:
Ω(1)

## Big Theta (Θ)

Represents the **exact or average bound**.

Example:
Θ(n)

---

# 7. Rules for Measuring Complexity

Rule 1
Assignment statements and simple conditions have complexity:

O(1)

Rule 2
A single loop running from 0 to n:

O(n)

Example:

```python
for i in range(n):
    print(i)
```

Rule 3
Nested loops result in quadratic complexity.

O(n²)

Example:

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Rule 4
When a loop divides the variable by 2 each iteration, the complexity becomes logarithmic.

O(log n)

Example:

```python
n = 16

while n > 1:
    print(n)
    n = n // 2
```

Rule 5
If multiple statements exist, add their complexities.

Example:

```
O(n) + O(n²) = O(n²)
```

We keep the dominant term.

---

# 8. Python Example – Reverse a Number

### Method 1 (Fixed 3-Digit Logic)

```python
no = int(input("Enter any value: "))

n1 = no % 10
no = no // 10

n2 = no % 10
n3 = no // 10

rev = n1 * 100 + n2 * 10 + n3
print(rev)
```

---

### Method 2 (General Algorithm – Recommended)

Works for numbers of any length.

```python
no = int(input("Enter number: "))
rev = 0

while no > 0:
    digit = no % 10
    rev = rev * 10 + digit
    no = no // 10

print(rev)
```

Time Complexity:

O(n)

where **n = number of digits**

---

# 9. Example of Logarithmic Complexity

```python
n = 16

while n > 1:
    print(n)
    n = n // 2
```

Output:

```
16
8
4
2
1
```

Each step reduces the problem size by half, so the time complexity is:

O(log n)

---

# Conclusion

Algorithms define the steps to solve a problem, while data structures organize the data used by those algorithms.
Big O notation helps measure the efficiency of algorithms, ensuring programs remain efficient as input sizes grow.
