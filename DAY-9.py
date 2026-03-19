QUESTION:Palindrome Number
https://leetcode.com/problems/palindrome-number/description/

ANSWER:
       class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original = x
        rev = 0
        
        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10
        
        return original == rev
_____________________________________________________________________________________________________________________________________________________________

QUESTION : Richest Customer Wealth
https://leetcode.com/problems/richest-customer-wealth/description/
ANSWER:
       class Solution:
    def maximumWealth(self, accounts):
        max_wealth = 0
        for i in accounts:
            total = sum(i)
            if total > max_wealth:
                max_wealth = total
        return max_wealth
____________________________________________________________________________________________________________________________________________________________________
QUESTION:Find Product
https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-product/
CODE:
      n = int(input())
arr = list(map(int, input().split()))

mod = 1000000007
result = 1

for num in arr:
    result = (result * num) % mod

print(result)
____________________________________________________________________________________________________________________________________________________________
QUESTION: Staircase
https://www.hackerrank.com/challenges/staircase/problem
CODE:

     n = int(input())

for i in range(1, n + 1):
    spaces = n - i
    hashes = i
    print(" " * spaces + "#" * hashes)
_____________________________________________________________________________________________________________________________________________________
QUESTION: Mini-Max Sum
https://www.hackerrank.com/challenges/mini-max-sum/problem
CODE
    arr = list(map(int, input().split()))

total = sum(arr)
min_sum = total - max(arr)
max_sum = total - min(arr)

print(min_sum, max_sum)
_________________________________________________________________________________________________________________________________________________________
OUESTION:Birthday Cake Candles
https://www.hackerrank.com/challenges/birthday-cake-candles/problem
CODES:n = int(input())
arr = list(map(int, input().split()))

tallest = max(arr)
count = arr.count(tallest)

print(count)
___________________________________________________________________________________________________________________________________________________
OUESTION:Time Conversion
https://www.hackerrank.com/challenges/time-conversion/problem
CODE:def timeConversion(s):
    period = s[-2:]       
    time = s[:-2]        
    hh, mm, ss = time.split(":")

    if period == "AM":
        if hh == "12":
            hh = "00"
    else:  # PM
        if hh != "12":
            hh = str(int(hh) + 12)

    return hh + ":" + mm + ":" + ss


s = input()
print(timeConversion(s))
___________________________________________________________________________________________________________________________________________________________________

