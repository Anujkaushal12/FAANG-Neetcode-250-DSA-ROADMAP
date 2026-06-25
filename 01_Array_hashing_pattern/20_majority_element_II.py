"""
LeetCode 229 — Majority Element II

Key Idea:-
        This problem asks us to find all elements that appear more than ⌊n/3⌋ times.

Important Observation:-
                    There can be at most 2 elements that appear more than n/3 times.

Why?
    If there were 3 such elements:
                                (n/3) + (n/3) + (n/3) > n   
                                
    which is impossible.

Therefore, we only need to keep track of at most two potential candidates.


Approach:-

Step 1: Candidate Selection
Traverse the array:
                ->Increase count if the element already exists.
                ->If there are more than 2 candidates:
                ->Decrease every candidate count by 1.
                ->Remove candidates whose count becomes 0.

This process eliminates non-majority elements.

Step 2: Verification
                    The remaining candidates are only potential majority elements.
"""

from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        # Stores candidate counts
        count = defaultdict(int)

        # First pass: find potential candidates
        for n in nums:
            count[n] += 1

            # At most 2 candidates can survive
            if len(count) <= 2:
                continue

            # Decrease all counts by 1
            new_count = defaultdict(int)

            for num, c in count.items():
                if c > 1:
                    new_count[num] = c - 1
            count = new_count

        # Second pass: verify candidates
        result = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                result.append(n)
        return result
    
"""
Complexity Summary
Complexity	     |    Value
Time Complexity	 |    O(n)
Space Complexity |    O(1)
"""