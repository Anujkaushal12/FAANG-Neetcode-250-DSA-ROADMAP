"""
Leetcode Problem Number:15

Key Idea & Approach:-
                The goal is to find all unique triplets that sum up to zero. A brute-force approach takes O(n³) time. You can optimize this to O(n²) using a Sorting + Two-Pointer approach:

1.)Sort the Array: Sorting groups duplicate numbers together, which makes it easy to skip them and avoid duplicate triplets.
2.)Fix the First Element: Iterate through the array with a loop. The current element acts as the first number of the triplet.
3.)Skip Duplicates (First Element): If the current number is the same as the previous one, skip it to prevent duplicate results.
4.)Two-Pointer Search: Initialize a left pointer (l) just after the fixed element and a right pointer (r) at the very end of the array.
5.)Adjust Pointers:
    If the sum is greater than zero, decrease the right pointer to get a smaller sum.
    If the sum is less than zero, increase the left pointer to get a larger sum.
    If the sum equals zero, save the triplet.
6.)Skip Duplicates (Remaining Elements): After finding a valid triplet, move the left pointer forward and continue moving it if the next element is a duplicates.

"""
from typing import List

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        # Step 1: Sort the array to use the two-pointer technique
        nums.sort()
        # Step 2: Iterate through the array to fix the first element
        for i, v in enumerate(nums):
            # Step 3: Skip duplicate values for the first element to avoid duplicate triplets
            if i > 0 and v == nums[i - 1]:
                continue
            # Step 4: Initialize two pointers for the remaining part of the array
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = v + nums[l] + nums[r]
                # Step 5: Adjust pointers based on the sum
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    # Found a valid triplet
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    # Step 6: Skip duplicate values for the second element
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1       
        return res
"""
Complexity:-
Time    :-      O(n)
Space   :-      O(n)
"""