"""
Key Idea:-
    Use a combination of:
        ->Hash Map (Dictionary) → for O(1) lookup by key.
        ->Doubly Linked List → for O(1) insertion and deletion.
Core Observation:-
    The cache maintains nodes in order of usage:
            LRU ←──────────────→ MRU
        Left = Least Recently Used (LRU)
        Right = Most Recently Used (MRU)
    ->Whenever a key is accessed (get) or inserted/updated (put), move its node to the MRU position (right end).
    ->If the cache exceeds its capacity, remove the LRU node from the left.

Approach:-
    1.Maintain a dictionary:
        key → node
    2.Use a doubly linked list with dummy head and tail nodes.
    3.get(key)
        If key exists:
            Remove its node.
            Insert it at the MRU end.
            Return its value.
        Otherwise return -1.
    4.put(key, value)
        If key already exists, remove its old node.
        Create and insert the new node at the MRU end.
        Add it to the dictionary.
        If the cache size exceeds capacity:
            Remove the LRU node.
            Delete it from the dictionary.
"""
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        # Previous and next pointers
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        
        # Maximum cache capacity
        self.cap = capacity

        # Maps key -> node
        self.cache = {}

        # Dummy head (LRU side) and dummy tail (MRU side)
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node from the doubly linked list
    def remove(self, node):

        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    # Insert a node before the dummy tail (MRU position)
    def insert(self, node):

        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:

        # Key exists
        if key in self.cache:

            # Move node to MRU position
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        # Key not found
        return -1

    def put(self, key: int, value: int) -> None:

        # Remove old node if key already exists
        if key in self.cache:
            self.remove(self.cache[key])

        # Create new node
        self.cache[key] = Node(key, value)

        # Insert at MRU position
        self.insert(self.cache[key])
        # Remove LRU node if capacity exceeded
        if len(self.cache) > self.cap:

            # First real node is the LRU
            lru = self.left.next

            # Remove it from linked list
            self.remove(lru)

            # Remove it from dictionary
            del self.cache[lru.key]