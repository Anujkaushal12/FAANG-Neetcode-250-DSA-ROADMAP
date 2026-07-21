"""
Key Idea:-
    ->Use a Hash Map (Dictionary) to map each original node to its copied node.
    ->Since each node contains both a next pointer and a random pointer, we cannot correctly connect the copied nodes until all copies have been created.

Core Observation:-
    ->Create the deep copy in two passes:
    ->First Pass: Create a copy of every node and store the mapping:
                                                                    Original Node → Copied Node
    ->Second Pass: Use the mapping to correctly assign the next and random pointers of each copied node.

Approach:-
    1.Create a dictionary oldToCopy with:
                                        {None: None}
        so None pointers are handled automatically.
    2.Traverse the original list and create a copy of every node.
    3.Store the mapping:
                        Original Node → Copied Node
    4.Traverse the list again.
    5.For each copied node:
                        Set its next pointer.
                        Set its random pointer.
    6..Return the copied head.
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Maps original nodes to their copied nodes
        oldToCopy = {None: None}

        # ---------- First Pass ----------
        # Create a copy of every node
        curr = head
        while curr:
            # Create copied node
            copy = Node(curr.val)
            # Store mapping
            oldToCopy[curr] = copy
            curr = curr.next

        # ---------- Second Pass ----------
        # Connect next and random pointers
        curr = head
        while curr:
            # Get copied node
            copy = oldToCopy[curr]
            # Connect next pointer
            copy.next = oldToCopy[curr.next]
            # Connect random pointer
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        # Return copied linked list
        return oldToCopy[head]