"""
Problem: LeetCode 217 - Contains Duplicate

Key Insights: The problem only asks if any duplicate exists, not how many, making it a perfect use case for a set to track uniqueness, which is faster than sorting.

Edge Case: Empty or Single Element: The loop should handle empty arrays ([]) or single-element arrays ([1]) correctly (returns false).

Detailed Approach: 
1.Hash SetInitialize an empty hash set (or hash map) to store visited integers.
2.Iterate through the array nums once.
3.For each element, check if it exists in the set.
   (i)If yes, return true (duplicate found).
   (ii)If no, insert the element into the set.
4.If the loop completes without finding a duplicate, return false

Alternative Sorting Approach: Sorting the array first takes (O(n \log n)) time and (O(1)) or (O(n)) space (depending on sorting algorithm) but is slower than hashing.
"""
from typing import List
#Hashing approach solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen={}
        for num in nums:
            if num in seen:
                return True
            seen[num]=True
        return False

"""
Time Complexity:
The time complexity of this approach is O(n), where n is the size of the input list. In the worst case, we might need to traverse the entire list once to find a duplicate.

Space Complexity:
The space complexity is O(n), as the hash set can potentially store all elements of the input list if they are all distinct.
"""
