# LeetCode 1929 — Concatenation of Array

# Key Idea:
# ->The goal is to create a new array containing two copies of the original array.

# ->We can achieve this by:
#     1.Creating an empty result list.
#     2.Traversing the original array twice.
#     3.Appending each element to the result list during each traversal.

# ->This produces an array of size 2n containing two consecutive copies of nums.

# ->Approach:
#    1.Initialize an empty list res.
#    2.Run a loop two times.
#    3.For each iteration, traverse every element in nums.
#    4.Append each element to res.
#    5.Return the resulting list.

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Store the concatenated array
        res = []
        # Traverse the array twice
        for i in range(2):
            for n in nums:
                res.append(n)
        return res

# Complexity Analysis
# Time Complexity
# Time Complexity: O(n)

# Space Complexity
# Space Complexity: O(n)
