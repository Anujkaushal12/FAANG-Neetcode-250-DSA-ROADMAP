"""
Key Idea:-
    ->Use Recursion.
    ->Instead of reversing the list iteratively, recursively reverse the rest of the list and then connect the current node to the end of the reversed portion.

Core Observation:-
    Suppose we have:
        1 → 2 → 3 → 4 → 5
    The recursive call reverses:
        2 → 3 → 4 → 5
    into
        5 → 4 → 3 → 2
    Then we simply connect:
        2 → 1
    Finally, set:
        1 → None
    to avoid creating a cycle.

Approach:-
    1.If the list is empty, return None.
    2.Assume the current node is the new head.
    3.Recursively reverse the remaining list.
    4.After recursion:
        ->Point the next node back to the current node.
        ->Disconnect the current node from its old next node.
    5.Return the new head.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list
        if not head:
            return None

        # Assume current node is the new head
        newHead = head

        # Reverse the remaining list recursively
        if head.next:
            newHead = self.reverseList(head.next)
            # Reverse the pointer
            head.next.next = head

        # Break the original forward link
        head.next = None

        # Return the new head of the reversed list
        return newHead
"""
| Complexity       | Value    |
| ---------------- | -------- |
| Time Complexity  | **O(n)** |
| Space Complexity | **O(n)** |
"""
