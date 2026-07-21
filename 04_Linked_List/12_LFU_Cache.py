"""
Key Idea:-
    ->Use a combination of:
        1.Hash Map → key → node for O(1) access.
        2.Frequency Map → frequency → doubly linked list.
        3.Doubly Linked Lists → maintain Least Recently Used (LRU) order among nodes with the same frequency.
Core Observation:-
    ->Each node stores:
        1.key
        2.value
        3.frequency
    ->Whenever a node is accessed or updated:
        1.Remove it from its current frequency list.
        2.Increase its frequency.
        3.Insert it into the next higher frequency list.

When the cache is full:
    ->Remove the Least Frequently Used node.
    ->If multiple nodes have the same frequency, remove the Least Recently Used among them.

Approach
get(key)
If key doesn't exist → return -1.
Increase its frequency.
Move the node into the next frequency list.
Return its value.
put(key, value)

If capacity is zero:

Return immediately.

If key already exists:

Update its value.
Increase its frequency.

Otherwise:

If cache is full:
Remove the least frequently used node.
Create a new node.
Insert it into frequency 1.
Set minimum frequency to 1.
"""
from collections import defaultdict

# Node of the doubly linked list
class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val

        # Initial frequency
        self.freq = 1

        self.prev = None
        self.next = None


# Doubly linked list for each frequency
class LinkedList:

    def __init__(self):

        # Dummy head and tail
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

        self.size = 0

    # Current size
    def length(self):
        return self.size

    # Insert node at MRU position
    def pushRight(self, node):

        prev = self.right.prev

        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node

        self.size += 1

    # Remove a node
    def pop(self, node):

        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

        node.prev = None
        node.next = None

        self.size -= 1

    # Remove LRU node
    def popLeft(self):

        if self.length() == 0:
            return None

        node = self.left.next
        self.pop(node)

        return node


class LFUCache:

    def __init__(self, capacity: int):

        self.cap = capacity

        # Current minimum frequency
        self.lfuCnt = 0

        # key -> node
        self.nodeMap = {}

        # frequency -> linked list
        self.listMap = defaultdict(LinkedList)

    # Increase node frequency
    def counter(self, node):

        freq = node.freq

        # Remove node from old frequency list
        self.listMap[freq].pop(node)

        # Update minimum frequency if needed
        if freq == self.lfuCnt and self.listMap[freq].length() == 0:
            self.lfuCnt += 1

        # Increase frequency
        node.freq += 1

        # Insert into new frequency list
        self.listMap[node.freq].pushRight(node)

    def get(self, key: int) -> int:

        if key not in self.nodeMap:
            return -1

        node = self.nodeMap[key]

        # Increase frequency
        self.counter(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        if self.cap == 0:
            return

        # Update existing key
        if key in self.nodeMap:

            node = self.nodeMap[key]
            node.val = value

            self.counter(node)
            return

        # Cache full -> remove LFU node
        if len(self.nodeMap) == self.cap:

            node = self.listMap[self.lfuCnt].popLeft()

            del self.nodeMap[node.key]

        # Create new node
        node = ListNode(key, value)

        self.nodeMap[key] = node

        # Insert into frequency 1 list
        self.listMap[1].pushRight(node)

        self.lfuCnt = 1