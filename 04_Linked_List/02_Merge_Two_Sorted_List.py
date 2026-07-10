"""
Key Idea:-
    ->Use Iteration + Dummy Node.
    ->Since both linked lists are already sorted, repeatedly choose the smaller node from the two lists and attach it to the merged list.

Core Observation:-
    ->Maintain a pointer (tail) that always points to the last node of the merged list.

    ->At each step:
        Compare the current nodes of l1 and l2.
        Attach the smaller node to tail.
        Move the corresponding list pointer forward.
        Advance tail.

    ->After one list is exhausted, append the remaining nodes of the other list.

Approach:-
    1.Create a dummy node to simplify edge cases.
    2.Initialize tail to point to the dummy node.
    3.While both lists are non-empty:
        ->Compare the values of the current nodes.
        ->Attach the smaller node to tail.
        ->Move the corresponding list pointer.
        ->Advance tail.
    4.Attach the remaining nodes from the non-empty list.
    5.Return dummy.next as the head of the merged list.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self,l1: Optional[ListNode],l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node simplifies list construction
        dummy = ListNode()

        # Tail points to the last node of the merged list
        tail = dummy

        # Compare nodes from both lists
        while l1 and l2:
            # Attach the smaller node
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            # Move tail forward
            tail = tail.next

        # Attach the remaining nodes
        if l1:
            tail.next = l1
        else:
            tail.next = l2

        # Return the merged list
        return dummy.next

"""
Time Complexity:-
                O(n + m)
Space Complexity:-
                O(1)
"""