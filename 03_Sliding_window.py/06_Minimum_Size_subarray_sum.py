"""
Key Idea:-
    Use a Sliding Window.
    Since all numbers in the array are positive, increasing the window size always increases (or maintains) the sum, and shrinking the window always decreases the sum.
    This property allows us to efficiently find the smallest valid subarray.
    Core Observation:-
        Maintain a window whose sum is:
                                Current Sum ≥ Target
        Whenever the window satisfies this condition:
                                Record its length.
                                Shrink it from the left to see if an even smaller valid window exists.

Approach:-
    1.Initialize:
        left = 0
        currentSum = 0
        minLength = ∞
    2.Expand the window by moving the right pointer.
    3.Add the current element to the running sum.
    4.While the current sum is at least the target:
                                Update the minimum length.
                                Remove the leftmost element.
                                Move the left pointer.
    5.If no valid subarray exists, return 0.
    6.Otherwise, return the minimum length found.
"""
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Left pointer of the sliding window
        left = 0
        # Current sum of the window
        currentSum = 0
        # Minimum valid window length
        minLength = float("inf")

        # Expand the window
        for right in range(len(nums)):
            # Add current element
            currentSum += nums[right]
            # Shrink the window while it satisfies the target
            while currentSum >= target:
                # Update minimum length
                minLength = min(minLength, right - left + 1)
                # Remove leftmost element
                currentSum -= nums[left]
                # Move left pointer
                left += 1
        # No valid subarray found
        return 0 if minLength == float("inf") else minLength

"""
| Complexity       | Value    |
| ---------------- | -------- |
| Time Complexity  | **O(n)** |
| Space Complexity | **O(1)** |

"""