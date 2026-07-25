from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts the list nums in-place so that all 0s come first, 
        followed by 1s, then 2s.
        Uses the Dutch National Flag algorithm.
        """
        
        l, r = 0, len(nums) - 1  # l = left boundary for 0s, r = right boundary for 2s
        i = 0  # current index pointer

        def swap(i: int, j: int) -> None:
            """Helper function to swap elements at indices i and j."""
            nums[i], nums[j] = nums[j], nums[i]

        # Process elements until i passes r
        while i <= r:
            if nums[i] == 0:
                # Swap current element with left boundary
                swap(l, i)
                l += 1
                i += 1  # Move forward since swapped element is already processed
            elif nums[i] == 2:
                # Swap current element with right boundary
                swap(i, r)
                r -= 1
                # Do NOT increment i here because swapped element at i needs checking
            # nums[i] == 1, just move forward
            i += 1