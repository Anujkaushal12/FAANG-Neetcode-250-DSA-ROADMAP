"""
LeetCode 704. Binary Search

Key Idea:-

Use Binary Search to efficiently locate the target in a sorted array by repeatedly dividing the search space in half.

Compare the middle element with the target.
If they are equal, return the index.
If the target is smaller, search the left half.
If the target is larger, search the right half.
Continue until the target is found or the search space becomes empty.

Approach:-
    1.Initialize two pointers:
        low = 0
        high = len(nums) - 1
    2.While low <= high:
        Compute the middle index.
        If the middle element equals the target, return its index.
        If the target is smaller than the middle element, search the left half by updating high.
        Otherwise, search the right half by updating low.
    3.If the loop ends without finding the target, return -1.
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize search boundaries
        low = 0
        high = len(nums) - 1

        # Continue searching while the search space is valid
        while low <= high:

            # Find the middle index
            mid = (low + high) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Search in the left half
            elif nums[mid] > target:
                high = mid - 1

            # Search in the right half
            else:
                low = mid + 1

        # Target does not exist
        return -1

"""
Time Complexity:-
                O(log n)
Space Complexity:-
                O(1)
"""