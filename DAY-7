https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/roy-and-profile-picture/
When any photo is uploaded following events may occur:

[1] If any of the width or height is less than L, user is prompted to upload another one. Print "UPLOAD ANOTHER" in this case.
[2] If width and height, both are large enough and
(a) if the photo is already square then it is accepted. Print "ACCEPTED" in this case.
(b) else user is prompted to crop it. Print "CROP IT" in this case.

ANSWER==
L = int(input())
N = int(input())

for _ in range(N):
    W, H = map(int, input().split())
    
    if W < L or H < L:
        print("UPLOAD ANOTHER")
    elif W == H:
        print("ACCEPTED")
    else:
        print("CROP IT")

___________________________________________________________________________________________________________________________________________________________________
https://www.hackerearth.com/problem/algorithm/monk-and-rotation-3-bcf1aefe/
question:
Input:
The first line will consists of one integer T denoting the number of test cases.
For each test case:
1) The first line consists of two integers N and K, N being the number of elements in the array and K denotes the number of steps of rotation.
2) The next line consists of N space separated integers , denoting the elements of the array A.

Output:
t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    k = k % n  
    
    result = arr[-k:] + arr[:-k]
    
    print(*result)
_________________________________________________________________________________________________________________________________________________________
You have been given a String S consisting of uppercase and lowercase English alphabets. You need to change the case of each alphabet in this String. That is, all the uppercase letters should be converted to lowercase and all the lowercase letters should be converted to uppercase. You need to then print the resultant String to output.

Input Format
The first and only line of input contains the String S

Output Format
Print the resultant String on a single line.

Constraints
 where S denotes the length of string S.

Sample Input
abcdE
Sample Output
ABCDe

Print the required array.

output
s = input()

result = ""

for ch in s:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)   # convert to uppercase
    elif 'A' <= ch <= 'Z':
        result += chr(ord(ch) + 32)   # convert to lowercase

print(result)

ouestion:
majorinty elemenjt
arr = list(map(int, input().split()))
n = len(arr) // 2

for i in arr:
    if arr.count(i) > n:
        print("Majority number:", i)
        break
else:
    print("No majority element")

## array
arr = list(map(int, input().split()))
n = len(arr)
result = [1] * n

left = 1
for i in range(n):
    result[i] = left
    left *= arr[i]

right = 1
for i in range(n - 1, -1, -1):
    result[i] *= right
    right *= arr[i]

print(result)
