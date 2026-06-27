"""
LeetCode Problem 26: Remove Duplicates from Sorted Array

Key Idea & Approach:-
The algorithm uses a Two-Pointer Approach to modify the array in-place. Because the input array is already sorted, all duplicate elements sit right next to each other.

->Left Pointer (l): Tracks the index where the next unique element should be written. It starts at index 1 because the very first element (index 0) is always unique.

->Right Pointer (r): Scans through the array from left to right, comparing each element with the one right before it (nums[r - 1]).

The Shift: Whenever the right pointer finds a new unique value (nums[r] != nums[r - 1]), it copies that value over to the left pointer's location and shifts the left pointer forward
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Handle edge case where the array is empty
        if not nums:
            return 0
        # 'l' is the write pointer for the next unique element position
        l = 1 
        # 'r' is the read pointer scanning the array starting from index 1
        for r in range(1, len(nums)):
            # If the current element is different from the previous one, it is unique
            if nums[r] != nums[r - 1]:
                # Overwrite the element at 'l' with this unique element
                nums[l] = nums[r]
                # Increment the write pointer
                l += 1
        # Return the count of unique elements (the length of the modified array prefix)
        return l


"""
Complexity:-
Time    :-      O(n)
Space   :-      O(1)
"""