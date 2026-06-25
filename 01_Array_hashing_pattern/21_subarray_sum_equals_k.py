"""
LeetCode 560 — Subarray Sum Equals K

Key Idea:-
        ->Use Prefix Sum + Hash Map.
        ->Instead of checking every possible subarray (O(n²)), we keep track of prefix sums seen so far.

Core Observation:-
    If:
        current_prefix_sum - previous_prefix_sum = k
    then:
        previous_prefix_sum = current_prefix_sum - k

So whenever we reach a new prefix sum, we check whether:
                                                    current_sum - k has been seen before.

If yes, every occurrence of that prefix sum represents a valid subarray ending at the current index whose sum equals k.

Approach:-
Initialize:
        ->curr_sum = 0
        ->res = 0
        ->prefixSums = {0: 1}
        ->Traverse the array:
            Add current element to curr_sum.
Compute:
        diff = curr_sum - k
        If diff exists in the hashmap, add its frequency to the answer.
        Store/update the frequency of curr_sum.
        Return the total count.

Why prefixSums = {0:1}?
                    This handles subarrays starting from index 0.
"""

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # Number of valid subarrays
        res = 0

        # Running prefix sum
        curr_sum = 0

        # Stores frequency of prefix sums
        prefixSums = {0: 1}

        for n in nums:

            # Update running sum
            curr_sum += n

            # Required previous prefix sum
            diff = curr_sum - k

            # Add all matching prefix sums
            res += prefixSums.get(diff, 0)

            # Store current prefix sum
            prefixSums[curr_sum] = 1 + prefixSums.get(curr_sum, 0)

        return res
"""
Complexity Analysis:-

Complexity	            Value
Time Complexity	 -->    O(n)
Space Complexity -->	O(n)
"""