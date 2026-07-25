"""
LeetCode 232. Implement Queue using Stacks

Key Idea"-
    ->Use two stacks to simulate FIFO (First In, First Out) queue behavior.
        Stack s1 is used for enqueue (push) operations.
        Stack s2 is used for dequeue (pop) and front (peek) operations.
        Transfer elements from s1 to s2 only when s2 is empty. This reverses the order, making the oldest element accessible at the top of s2.


Approach:-
    1.Maintain two stacks:
        s1 → stores newly added elements.
        s2 → stores elements in queue order for removal.
    2.Push:
        Push the new element onto s1.
    3.Pop:
        If s2 is empty, move all elements from s1 to s2.
        Pop and return the top element from s2.
    4.Peek:
        If s2 is empty, transfer all elements from s1 to s2.
        Return the top element of s2, which represents the front of the queue.
    5.Empty:
        The queue is empty only if both stacks are empty.
"""

class MyQueue:

    def __init__(self):
        # Stack for enqueue operations
        self.s1 = []

        # Stack for dequeue and peek operations
        self.s2 = []

    def push(self, x: int) -> None:
        # Add the element to the input stack
        self.s1.append(x)

    def pop(self) -> int:
        # Transfer elements only when the output stack is empty
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        # Remove and return the front element
        return self.s2.pop()

    def peek(self) -> int:
        # Transfer elements only when needed
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        # Return the front element without removing it
        return self.s2[-1]

    def empty(self) -> bool:
        # Queue is empty only if both stacks are empty
        return len(self.s1) == 0 and len(self.s2) == 0

"""
| Operation   | Complexity         |
| ----------- | ------------------ |
| **push()**  | **O(1)**           |
| **pop()**   | **O(1)** amortized |
| **peek()**  | **O(1)** amortized |
| **empty()** | **O(1)**           |
"""