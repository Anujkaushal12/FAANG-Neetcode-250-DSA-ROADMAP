from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize the maximum area tracking variable
        res = 0
        
        # Initialize two pointers at the absolute boundaries of the array
        # 'l' starts at the first line, 'r' starts at the last line
        l, r = 0, len(height) - 1
        
        # Loop until the two pointers meet each other
        while l < r:
            # The height of water is dictated by the shorter of the two boundaries.
            # The width of the container is the horizontal distance between pointers (r - l).
            area = min(height[l], height[r]) * (r - l)
            
            # Keep track of the largest container capacity found so far
            res = max(area, res)
            
            # Greedy step: Shift the pointer pointing to the shorter vertical line inward.
            # Moving the taller line would never increase area because the width decreases
            # and the water level remains bottlenecked by the shorter line anyway.
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return res
