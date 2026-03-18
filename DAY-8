1ST:Two Sum
https://leetcode.com/problems/two-sum/description/
CODE:
      class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in d:
                return [d[diff], i]
            
            d[nums[i]] = i
_________________________________________________________________________________________________________________________________________________________________
2nd: Fizz Buzz
https://leetcode.com/problems/fizz-buzz/description/
code: 
     class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer
________________________________________________________________________________________________________________________________________________________
3rd: Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/description/
code:
     class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums
        __________________________________________________________________________________________________________________________________________________
4th:implement a stack push pop peek and disaplay code in python
code:
     class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.stack = []

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

    def push(self, element):
        # Add an element to the top of the stack
        self.stack.append(element)
        print(f"Pushed item: {element}")

    def pop(self):
        # Remove and return the top element from the stack
        if self.is_empty():
            return "Stack is empty (Underflow)"
        return self.stack.pop()

    def peek(self):
        # View the top element without removing it
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def display(self):
        # Print all elements in the stack
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack contents:", self.stack)

# Example Usage
if __name__ == "__main__":
    my_stack = Stack()

    print("--- Stack Operations Demonstration ---")
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    my_stack.display()

    print(f"\nPeek: {my_stack.peek()}")

    popped_item = my_stack.pop()
    print(f"Popped item: {popped_item}")
    my_stack.display()

    my_stack.pop()
    my_stack.pop()
    popped_item_empty = my_stack.pop() # Attempting to pop from an empty stack
    print(f"Attempted pop on empty stack: {popped_item_empty}")
    my_stack.display()
__________________________________________________________________________________________________________________________________________________________
5th:print next larger elemenet input n=4 ,array=[1 3 2 4] in python
  code:
       def find_next_larger_elements(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result

n = 4
array = [1, 3, 2, 4]
output = find_next_larger_elements(array)
print(*output)

n = 4
array = [1, 3, 2, 4]
output = find_next_larger_elements(array)
print(output)
