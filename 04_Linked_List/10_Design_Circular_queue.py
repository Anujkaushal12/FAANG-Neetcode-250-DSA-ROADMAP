"""
Key Idea:-
    ->Implement a Circular Queue using a Doubly Linked List with dummy head and tail nodes.
    ->Instead of physically arranging nodes in a circle, maintain:
        A dummy head (left)
        A dummy tail (right)
        A variable space to track the remaining capacity.
    ->This simplifies insertion and deletion by avoiding edge cases.

Approach:-
    1.Initialize:
        space = k
        Dummy head (left)
        Dummy tail (right)
    2.enQueue(value)
        If full, return False.
        Insert a new node before the dummy tail.
        Decrease available space.
    3.deQueue()
        If empty, return False.
        Remove the node after the dummy head.
        Increase available space.
    4.Front()
        Return the first element.
    5.Rear()
        Return the last element.
    6.isEmpty()
        Check if the list contains only the dummy nodes.
    7.isFull()
        Check if no space remains.
"""
class ListNode:
    def __init__(self, prev, val, next):
        self.prev = prev
        self.val = val
        self.next = next


class MyCircularQueue:
    def __init__(self, k: int):
        # Remaining available capacity
        self.space = k
        # Dummy head node
        self.left = ListNode(None, 0, None)
        # Dummy tail node
        self.right = ListNode(self.left, 0, None)
        # Connect dummy nodes
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:

        # Queue is full
        if self.space == 0:
            return False

        # Create a new node before the dummy tail
        node = ListNode(self.right.prev, value, self.right)
        # Connect previous last node to new node
        self.right.prev.next = node
        # Update tail's previous pointer
        self.right.prev = node
        # Decrease available space
        self.space -= 1

        return True

    def deQueue(self) -> bool:

        # Queue is empty
        if self.isEmpty():
            return False

        # Remove the first real node
        self.left.next = self.left.next.next
        # Update previous pointer
        self.left.next.prev = self.left
        # Increase available space
        self.space += 1

        return True

    def Front(self) -> int:

        # Queue is empty
        if self.isEmpty():
            return -1

        # First element
        return self.left.next.val

    def Rear(self) -> int:

        # Queue is empty
        if self.isEmpty():
            return -1

        # Last element
        return self.right.prev.val

    def isEmpty(self) -> bool:

        # No real nodes exist
        return self.left.next == self.right

    def isFull(self) -> bool:

        # No remaining capacity
        return self.space == 0

"""
| Operation   | Time     | Space    |
| ----------- | -------- | -------- |
| `enQueue()` | **O(1)** | **O(1)** |
| `deQueue()` | **O(1)** | **O(1)** |
| `Front()`   | **O(1)** | **O(1)** |
| `Rear()`    | **O(1)** | **O(1)** |
| `isEmpty()` | **O(1)** | **O(1)** |
| `isFull()`  | **O(1)** | **O(1)** |
"""