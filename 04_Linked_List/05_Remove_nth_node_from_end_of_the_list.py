"""
Key Idea:-
    ->Use Two Pointers + Dummy Node.
    ->Maintain a gap of n nodes between the right and left pointers.
    ->When the right pointer reaches the end of the list, the left pointer will be positioned just before the node that needs to be removed.
    ->Using a dummy node simplifies handling edge cases, such as removing the head node.

Approach:-
    1.Create a dummy node pointing to the head.
    2.Initialize:
        ->left at the dummy node.
        ->right at the head.
    3.Move the right pointer n steps ahead.
    4.Move both pointers together until right reaches the end.
    5.left.next is now the node to remove.
    6.Skip the target node by updating:
        left.next = left.next.next
    7.Return dummy.next.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self,head: Optional[ListNode],n: int) -> Optional[ListNode]:
        # Dummy node simplifies removing the head node
        dummy = ListNode(0, head)

        # Initialize two pointers
        left = dummy
        right = head

        # Move right pointer n steps ahead
        while n > 0 and right:
            right = right.next
            n -= 1

        # Move both pointers together
        while right:
            left = left.next
            right = right.next

        # Remove the nth node from the end
        left.next = left.next.next

        # Return the updated list
        return dummy.next

"""
Time Complexity:-
                O(n)
Space Complexity:-
                O(1)
"""