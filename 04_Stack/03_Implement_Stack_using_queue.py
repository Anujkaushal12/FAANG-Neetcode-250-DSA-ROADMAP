"""
LeetCode 225. Implement Stack using Queues

Key Idea:-
    Simulate LIFO (Last In, First Out) stack behavior using a single queue (FIFO). To remove the top element, rotate the queue until the last inserted element reaches the front, then dequeue it.

Approach:-
    1.Use a single queue (deque) to store the elements.
    2.Push:
        Simply enqueue the new element at the back of the queue.
    3.Pop:
        Rotate the queue by moving the first n - 1 elements to the back.
        The remaining front element is the most recently inserted (stack top), so dequeue and return it.
    4.Top:
        Return the last element of the queue since it represents the top of the stack.
    5.Empty:
        Return True if the queue has no elements; otherwise, return False.
"""

from collections import deque

class MyStack:

    def __init__(self):
        # Queue used to simulate stack operations
        self.q = deque()

    def push(self, x: int) -> None:
        # Insert the element at the back of the queue
        self.q.append(x)

    def pop(self) -> int:
        # Rotate the first n-1 elements to the back
        # so the last inserted element comes to the front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

        # Remove and return the stack's top element
        return self.q.popleft()

    def top(self) -> int:
        # The last element in the queue is the stack's top
        return self.q[-1]

    def empty(self) -> bool:
        # Return True if the stack is empty
        return len(self.q) == 0

"""
| Operation   | Complexity |
| ----------- | ---------- |
| **push()**  | **O(1)**   |
| **pop()**   | **O(n)**   |
| **top()**   | **O(1)**   |
| **empty()** | **O(1)**   |
"""