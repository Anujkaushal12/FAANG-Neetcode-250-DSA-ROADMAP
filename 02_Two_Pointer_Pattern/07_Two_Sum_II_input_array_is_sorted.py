"""
LeetCode Problem 167: Two Sum II - Input Array Is Sorted.

Key Idea Approach:-
The code implements the Two-Pointer Technique, which relies on the array being strictly sorted in ascending order.
->Two pointers are initialized: l (left) at the start 0, and r (right) at the end of the array.
->In each iteration, it calculates the sum of elements at both pointers (curr_sum).
->If curr_sum exactly equals the target, it returns the indices. Because LeetCode 167 requires 1-indexed results, it returns [l+1, r+1].
->If curr_sum is greater than the target, the right pointer moves left (r -= 1) to reduce the total sum.
->If curr_sum is less than the target, the left pointer moves right (l += 1) to increase the total sum.
"""
from typing import List

class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        # Initialize two pointers at opposite ends of the sorted array
        l, r = 0, len(num) - 1
        # Continue searching while the left pointer is strictly less than the right pointer
        while l < r:
            curr_sum = num[l] + num[r] # Calculate sum of current pair
            if curr_sum == target:
                # Return 1-based indices as required by the problem statement
                return [l + 1, r + 1]
            elif curr_sum > target:
                # If sum is too large, move the right pointer inward to get a smaller value
                r -= 1
            else:
                # If sum is too small, move the left pointer inward to get a larger value
                l += 1
        # Return an empty list if no such pair is found
        return []

"""
Time complexity:- O(n)
Space complexity:- O(1)
"""