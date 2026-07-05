"""
Key Idea:-
    ->Use a Sliding Window + Hash Set.
    ->The problem asks whether there are two equal elements such that: 
                                                                     |i - j| ≤ k
    Instead of comparing every pair (which takes O(n²)), maintain a sliding window of at most k previous elements.

Strategy:-
        ->Use a set to store the elements currently inside the window.
        ->Expand the window by moving the right pointer.
        ->If the window size exceeds k, remove the leftmost element.
        ->Before adding the current element, check whether it already exists in the set.
        ->If it does, a duplicate within distance k has been found.

Approach:-
    1.Initialize:
        A hash set window
        Left pointer L = 0
    2.Traverse the array using the right pointer R.
    3.If the window size exceeds k:
        Remove nums[L] from the set.
        Increment L.
    4.Check if nums[R] already exists in the set.
        If yes, return True.
    5.Otherwise, add nums[R] to the set.
    6.If no duplicate is found, return False.
"""
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # Stores elements currently inside the sliding window
        window = set()
        # Left pointer of the window
        left = 0

        # Traverse the array
        for right in range(len(nums)):

            # Maintain window size <= k
            if right - left > k:
                window.remove(nums[left])
                left += 1

            # Duplicate found within the window
            if nums[right] in window:
                return True
            
            # Add current element to the window
            window.add(nums[right])
        return False

"""
Complexity	Value
Time Complexity	    -->     O(n)
Space Complexity	-->     O(min(n, k))
"""