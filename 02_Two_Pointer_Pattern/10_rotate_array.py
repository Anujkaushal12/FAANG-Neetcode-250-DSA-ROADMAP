from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Normalize k. If k is greater than the length of nums,
        # rotating it k times is equivalent to rotating it k % len(nums) times.
        k = k % len(nums)
        
        # Step 2: Reverse the entire array
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]  # Swap elements at l and r
            l, r = l + 1, r - 1
            
        # Step 3: Reverse the first k elements (from index 0 to k-1)
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]  # Swap elements at l and r
            l, r = l + 1, r - 1
            
        # Step 4: Reverse the remaining elements (from index k to the end)
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]  # Swap elements at l and r
            l, r = l + 1, r - 1
