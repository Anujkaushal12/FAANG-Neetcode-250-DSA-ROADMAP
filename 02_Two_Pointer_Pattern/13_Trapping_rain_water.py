"""
Key Idea:-
    ->Use the Two Pointers technique.
    ->For each bar, the amount of trapped water depends on:
        Water = min(Max Height on Left, Max Height on Right) - Current Height
    ->Instead of precomputing left and right maximum arrays (which requires extra space), maintain:
        leftMax → Highest bar seen from the left.
        rightMax → Highest bar seen from the right.
    At every step:
        If leftMax < rightMax, the trapped water at the left pointer is determined only by leftMax.
        Otherwise, the trapped water at the right pointer is determined only by rightMax.


Approach:-
    1.If the array is empty, return 0.
    2.Initialize:
        left = 0
        right = n - 1
        leftMax = height[left]
        rightMax = height[right]
    3.While left < right:
        ->If leftMax < rightMax:
            Move the left pointer.
            Update leftMax.
            Add trapped water.
        ->Otherwise:
            Move the right pointer.
            Update rightMax.
            Add trapped water.
    4.Return the total trapped water.
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case: empty array
        if not height:
            return 0
        
        # Two pointers
        left = 0
        right = len(height) - 1

        # Maximum heights seen so far
        leftMax = height[left]
        rightMax = height[right]

        # Total trapped water
        water = 0

        # Process until pointers meet
        while left < right:
            # Left side is the limiting boundary
            if leftMax < rightMax:
                # Move left pointer
                left += 1
                # Update left maximum
                leftMax = max(leftMax, height[left])
                # Water trapped at current position
                water += leftMax - height[left]
            # Right side is the limiting boundary
            else:
                # Move right pointer
                right -= 1
                # Update right maximum
                rightMax = max(rightMax, height[right])
                # Water trapped at current position
                water += rightMax - height[right]
        return water
"""
Complexity Analysis
Time Complexity	    -->     O(n)
Space Complexity	-->     O(1)
"""