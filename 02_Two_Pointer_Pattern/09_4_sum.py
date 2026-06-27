from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort the array to enable the two-pointer approach and easily skip duplicates
        nums.sort()
        res, quad = [], []
        
        def Ksum(k, start, target):
            # Base Case: When k is not 2, use recursion to lock down numbers
            if k != 2:
                # Iterate through valid boundaries; leave enough space for remaining elements
                for i in range(start, len(nums) - k + 1):
                    # Skip duplicate elements to ensure unique combinations
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    
                    quad.append(nums[i])  # Add current number to the path
                    Ksum(k - 1, i + 1, target - nums[i])  # Recurse for K-1 sum
                    quad.pop()  # Backtrack to try the next number
                return

            # Base Case: When k == 2, solve using the classic Two-Pointer technique
            l, r = start, len(nums) - 1
            while l < r:
                current_sum = nums[l] + nums[r]
                
                if current_sum > target:
                    r -= 1  # Sum is too large; move the right pointer leftward
                elif current_sum < target:
                    l += 1  # Sum is too small; move the left pointer rightward
                else:
                    # Found a valid combination; append the path + current pair
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    
                    # Skip identical elements for the left pointer to avoid duplicate solutions
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                        
        # Kick off the recursive framework for a 4-Sum problem starting from index 0
        Ksum(4, 0, target)
        return res
