# Python Programs (Formatted Version)

---

## 1]

```python
# #n=int(input("Enter n: "))
# x=int(input("Enter n: "))
# sum=1
# for i in range(1,n):
#     sum=sum+(x**i)/i;
# print(sum)
```

**Output**

```
op : 2 3 = 4
```

---

## 2]

```python
# for i in range(1,5):        # outer loop - rows
#     for j in range(1,5):    # inner loop - columns
#         print(i,end="")     # i → 1111,2222   j → 1234,1234
#     print()
```

**Output**

```
1111
2222
3333
4444
```

---

## 3]

```python
# n=1
# for i in range(1,5):
#     for j in range(1,5):
#         print(n,end="\t")
#         n=n+1
#     print()
```

**Output**

```
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16
```

---

## 4]

```python
# n=65
# for i in range(1,5):
#     for j in range(1,5):
#         print(chr(n),end="\t")
#         n=n+1
#     print()
```

```python
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()
```

**Output**

```
1
22
333
4444
```

---

## 5]

```python
# for i in range(1,5):
#     for j in range(5-i):
#         print("*",end="\t")
#     print()
```
