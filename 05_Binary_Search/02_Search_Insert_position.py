"""
LeetCode 35. Search Insert Position

Key Idea:-
    Use Binary Search to find the target in a sorted array. If the target is not present, the left pointer (l) will indicate the correct position where it should be inserted to maintain the sorted order.

Approach:-
    1.Initialize two pointers:
        l = 0
        r = len(nums) - 1
    2.While l <= r:
        Find the middle index m.
        If nums[m] equals the target, return m.
        If nums[m] is smaller than the target, search the right half.
        Otherwise, search the left half.
    3.If the target is not found, return l, which represents the correct insertion index.
"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize search boundaries
        l, r = 0, len(nums) - 1

        # Perform binary search
        while l <= r:
            m = (l + r) // 2

            # Target found
            if nums[m] == target:
                return m

            # Search in the right half
            elif nums[m] < target:
                l = m + 1

            # Search in the left half
            else:
                r = m - 1

        # Target not found
        # 'l' is the correct insertion position
        return l

"""
Time Complexity:-
                O(log n)
Space Complexity:-
                O(1)
"""