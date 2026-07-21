"""
Key Idea:-
    ->Use Divide and Conquer.
    ->Instead of merging all k linked lists one by one, repeatedly merge them in pairs until only one sorted linked list remains.
    ->This is similar to the Merge Sort technique and significantly improves performance.

Core Observation:-
    At each round:
        1.Merge every two adjacent linked lists.
        2.Replace the original list of lists with the merged results.
        3.Repeat until only one list remains.

Example:
    L1   L2   L3   L4
            ↓
        Merge pairs
    (L1+L2)   (L3+L4)
            ↓
        Merge again
    ((L1+L2) + (L3+L4))

Approach:-
    1.If the input list is empty, return None.
    2.While more than one linked list exists:
    3.Merge every two adjacent linked lists.
    4.Store the merged lists in a new array.
    5.Replace the original array with the merged array.
    6.Return the only remaining merged linked list.
    7.Use a helper function (mergeLists) to merge two sorted linked lists.
"""
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self,lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # No linked lists
        if not lists or len(lists) == 0:
            return None

        # Continue until only one merged list remains
        while len(lists) > 1:

            mergedLists = []

            # Merge lists in pairs
            for i in range(0, len(lists), 2):

                l1 = lists[i]

                # Handle odd number of lists
                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                # Merge two sorted lists
                mergedLists.append(self.mergeLists(l1, l2))

            # Update list of merged lists
            lists = mergedLists

        return lists[0]

    # Merge two sorted linked lists
    def mergeLists(self, l1, l2):

        dummy = ListNode()
        tail = dummy

        # Compare nodes from both lists
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        # Attach remaining nodes
        if l1:
            tail.next = l1
        else:
            tail.next = l2

        return dummy.next