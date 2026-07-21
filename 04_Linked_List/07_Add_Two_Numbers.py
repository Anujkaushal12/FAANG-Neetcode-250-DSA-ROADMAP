"""
Key Idea:-
    ->Use Linked List Traversal + Carry Simulation.
    ->Each linked list represents a non-negative integer where the digits are stored in reverse order.
    ->Traverse both lists simultaneously, add corresponding digits along with the carry, and build the answer as a new linked list.

Core Observation:-
    ->For each position:
        digit = (value1 + value2 + carry) % 10
        carry = (value1 + value2 + carry) // 10
    ->Continue until:
        Both lists are exhausted.
        No carry remains.

Approach:-
    1.Create a dummy node for the result list.
    2.Initialize:
        current pointer.
        carry = 0.
    3.Traverse both linked lists simultaneously.
    4.Read the current digit from each list (or 0 if the list has ended).
    5.Compute:
        New digit.
        New carry.
    6.Create a new node containing the computed digit.
    7.Move all pointers forward.
    8.Return dummy.next
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self,l1: Optional[ListNode],l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node for the result list
        dummy = ListNode()
        # Pointer used to build the answer
        current = dummy
        # Carry from the previous addition
        carry = 0

        # Continue while either list has nodes or carry exists
        while l1 or l2 or carry:
            # Current digit from first list
            value1 = l1.val if l1 else 0
            # Current digit from second list
            value2 = l2.val if l2 else 0
            
            # Calculate total sum
            total = value1 + value2 + carry

            # Compute new carry
            carry = total // 10

            # Current digit to store
            digit = total % 10

            # Create a new node
            current.next = ListNode(digit)

            # Move current pointer
            current = current.next

            # Move list pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the resulting linked list
        return dummy.next
"""
| Complexity       | Value                                      |
| ---------------- | ------------------------------------------ |
| Time Complexity  | **O(max(m, n))**                           |
| Space Complexity | **O(max(m, n))** *(excluding input lists)* |
"""