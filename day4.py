# Functions, Lists, and Strings (Formatted Version)

---

## Functions

### 1. Function without Parameters

```python
# def add():
#     a=int(input("Enter Value: "))
#     b=int(input("Enter Value: "))
#     res=a+b
#     print(res)

# if __name__ =='__main__':
#     add()
```

---

### 2. Function with Parameters

```python
# def add(x,y):
#     res=a+b
#     print(res)

# if __name__ =='__main__':
#     a=int(input("Enter Value: "))
#     b=int(input("Enter Value: "))
#     add(a,b)
```

---

### 3. Function with Return Value

```python
# def add(x,y):
#     res=a+b
#     return res

# if __name__ =='__main__':
#     a=int(input("Enter Value: "))
#     b=int(input("Enter Value: "))
#     res=add(a,b)
#     print(res)
```

---

## Multiple Returning Values

```python
# def cal(x,y):
#     res1=a+b
#     res2=a-b
#     res3=a*b
#     res4=a/b
#     return res1, res2, res3, res4

# if __name__ =='__main__':
#     a=int(input("Enter Value: "))
#     b=int(input("Enter Value: "))
#     r1, r2, r3, r4 = cal(a,b)
#     print(r1,r2,r3,r4)
```

---

## Lists

```python
# ls=[]
# print(type(ls))

# ls=list()
# print(type(ls))
```

```python
# ls=[11,22,33,44,55,66]
# print(ls)

# for i in range(len(ls)):
#     print(ls[i])

# for x in ls:
#     print(x)
```

```python
# ls.append(12)
# ls.append(34)
# print(ls)
```

```python
# print(ls[0])
# print(ls[-6])
# print(ls[2:3])
# print(ls[::2])
# print(ls[::-2])
# print(ls[::-1])
```

---

## Strings

```python
# s="Ashish"
# print(s[1:3])
# print(s[::-1])

# a=1234
# print(len(str(a)))
# print(type(s))
```

---

## String Reverse Example

```python
a="tejas"
b=""

for i in a:
    b=i+b

print(b)
#reverse string
name = input("Enter your name: ")
rev = ""

for ch in name:
    rev = ch + rev

print("Reverse name:", rev)
```
