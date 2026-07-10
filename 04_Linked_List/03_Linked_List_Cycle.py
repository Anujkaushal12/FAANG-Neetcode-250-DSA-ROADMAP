"""
Key Idea:-
    Use Floyd's Cycle Detection Algorithm (Tortoise and Hare).
    Maintain two pointers:
        Slow Pointer → moves one node at a time.
        Fast Pointer → moves two nodes at a time.
Core Observation:-
    If there is no cycle, the fast pointer reaches None.
    If there is a cycle, the fast pointer eventually catches the slow pointer inside the cycle.

Approach:-
    1.Initialize both pointers at the head.
    2.Move:
        slow by one step.
        fast by two steps.
    3.If slow == fast, a cycle exists.
    4.If fast reaches the end, no cycle exists.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Initialize slow and fast pointers
        slow = head
        fast = head

        # Traverse the list
        while fast and fast.next:
            # Slow moves one step
            slow = slow.next
            # Fast moves two steps
            fast = fast.next.next
            # Cycle detected
            if slow == fast:
                return True
            
        # Fast reached the end
        return False
    
"""
| Complexity       | Value    |
| ---------------- | -------- |
| Time Complexity  | **O(n)** |
| Space Complexity | **O(1)** |
"""