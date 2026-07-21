"""
Key Idea:-
    ->Use Pointer Manipulation + Partial Linked List Reversal.
    ->Instead of reversing the entire linked list, reverse only the nodes between positions left and right, then reconnect the reversed portion with the remaining parts of the list.

Core Observation:-
    ->The algorithm consists of three steps:
        1.Reach the node just before position left.
        2.Reverse the sublist from left to right.
        3.Reconnect the reversed sublist with the first and last parts of the original list.
    ->Using a dummy node simplifies the case when left = 1.

Approach:-
    1.Create a dummy node pointing to the head.
    2.Move leftPrev to the node just before position left.
    3.Reverse the nodes from left to right.
    4.Connect:
        The last node before the reversed section to the new head of the reversed section.
        The original first node of the reversed section (now the tail) to the remaining list.
    5.Return dummy.next.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self,head: Optional[ListNode],left: int,right: int) -> Optional[ListNode]:
        # Dummy node simplifies reversing from the head
        dummy = ListNode(0, head)
        # Pointer to the node before the reversal starts
        leftPrev = dummy
        # Current node
        curr = head

        # Step 1: Reach the node at position 'left'
        for _ in range(left - 1):
            leftPrev = curr
            curr = curr.next

        # Step 2: Reverse nodes from left to right
        prev = None
        for _ in range(right - left + 1):
            # Store next node
            nextNode = curr.next
            # Reverse current pointer
            curr.next = prev
            # Move pointers
            prev = curr
            curr = nextNode

        # Step 3: Reconnect the reversed sublist

        # Original left node is now the tail of the reversed sublist
        leftPrev.next.next = curr

        # Connect node before left to new head of reversed sublist
        leftPrev.next = prev

        # Return updated list
        return dummy.next
"""
| Complexity       | Value    |
| ---------------- | -------- |
| Time Complexity  |   O(n)   |
| Space Complexity |   O(1)   |
"""