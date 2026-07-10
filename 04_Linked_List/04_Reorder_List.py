"""
Key Idea:-
    ->Use Three Steps:
        Find the middle of the linked list using Slow & Fast pointers.
        Reverse the second half of the list.
        Merge the two halves alternately.

This achieves the required order:
                                L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
without using extra space.

Approach:-
    1.Use slow and fast pointers to find the middle node.
    2.Split the list into two halves.
    3.Reverse the second half.
    4.Merge the first half and reversed second half by alternating nodes.
    5.The list is reordered in-place.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Step 1: Find the middle of the linked list
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        second = slow.next
        # Split the list into two halves
        prev = slow.next = None

        while second:
            # Store next node
            temp = second.next
            # Reverse current pointer
            second.next = prev
            # Move pointers
            prev = second
            second = temp

        # Step 3: Merge the two halves alternately
        first = head
        second = prev

        while second:
            # Save next nodes
            temp1 = first.next
            temp2 = second.next
            # Alternate nodes
            first.next = second
            second.next = temp1
            # Move both pointers
            first = temp1
            second = temp2