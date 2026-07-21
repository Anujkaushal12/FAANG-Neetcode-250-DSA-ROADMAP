"""
Key Idea:-
    ->Use Floyd's Cycle Detection Algorithm (Tortoise and Hare).
    ->Treat the array as a linked list where:
    ->Each index is a node.
    ->The value at each index points to the next node.
    ->Since one number is duplicated, two indices point to the same value, creating a cycle.
    ->The entry point of the cycle is the duplicate number.

Approach:-
    ->The algorithm consists of two phases.
        Phase 1: Detect the Cycle
            ->Initialize two pointers:
            ->slow moves one step.
            ->fast moves two steps.
            ->Continue until they meet.
        Phase 2: Find the Cycle Entrance
            ->Start another pointer (slow2) from index 0.
            ->Move both slow and slow2 one step at a time.
            ->The node where they meet is the duplicate number.
"""
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Detect the cycle
        slow = 0
        fast = 0

        while True:
            # Move slow by one step
            slow = nums[slow]
            # Move fast by two steps
            fast = nums[nums[fast]]
            # Cycle detected
            if slow == fast:
                break

        # Phase 2: Find the entrance of the cycle
        slow2 = 0

        while True:
            # Move both pointers one step
            slow = nums[slow]
            slow2 = nums[slow2]
            # Duplicate number found
            if slow == slow2:
                return slow

"""
Time Complexity:-
                O(n)
Space Complexity:-
                O(1)
"""