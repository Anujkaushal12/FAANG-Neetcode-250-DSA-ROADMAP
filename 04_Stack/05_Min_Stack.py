"""
LeetCode 155. Min Stack

Note: This implementation correctly supports all required stack operations, but getMin() scans the entire stack every time it is called. Therefore, it does not achieve the optimal O(1) minimum retrieval expected by the problem.

Key Idea:-
    Use a normal stack to store all elements. Whenever the minimum element is requested, traverse the stack to find the smallest value.

Approach:-
    1.Maintain a single stack (s1) to store elements.
    2.Push:
        Add the new element to the top of the stack.
    3.Pop:
        Remove the top element from the stack.
    4.Top:
        Return the top element without removing it.
    5.Get Minimum:
        Initialize the first element as the minimum.
        Traverse the remaining elements in the stack.
        Update the minimum whenever a smaller value is found.
        Return the smallest element.
"""

class MinStack:

    def __init__(self):
        # Stack to store all elements
        self.s1 = []

    def push(self, value: int) -> None:
        # Push the element onto the stack
        self.s1.append(value)

    def pop(self) -> None:
        # Remove the top element
        return self.s1.pop()

    def top(self) -> int:
        # Return the top element without removing it
        return self.s1[-1]

    def getMin(self) -> int:
        # Assume the first element is the minimum
        min_val = self.s1[0]

        # Traverse the stack to find the minimum value
        for num in self.s1[1:]:
            if num < min_val:
                min_val = num

        return min_val

"""
| Operation    | Complexity |
| ------------ | ---------- |
| **push()**   | **O(1)**   |
| **pop()**    | **O(1)**   |
| **top()**    | **O(1)**   |
| **getMin()** | **O(n)**   |
"""