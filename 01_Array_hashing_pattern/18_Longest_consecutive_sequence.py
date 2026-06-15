"""
Key Idea::-
1. Use a HashSet for O(1) lookup and only start counting sequences from numbers that are the beginning of a sequence.
2. A number is considered a sequence start if:  (num-1 not belongs to set).
3.Then keep expanding forward: num+1, num+2, num+3….
4.This avoids checking the same sequence multiple times.

Detailed Approach:-
1. Convert the array into a set for fast lookup.
2. Iterate through each unique number.
3. Check if the current number is the start of a sequence:
4. If num - 1 is not present.
5. Start counting consecutive numbers using a while loop.
6. Update the maximum streak length.
7.Return the longest streak.
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Edge case: if array is empty
        if not nums:  
            return 0

        num_set = set(nums)  # Store all numbers in a set for O(1) lookup
        longest_streak = 0  # Stores the length of longest sequence found

        # Iterate through unique numbers
        for num in num_set:

            # Check if current number is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Continue while next consecutive number exists
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)    # Update longest sequence length

        return longest_streak

# Time Complexity:- O(n)
# Each element is visited at most once in the sequence expansion.
# HashSet lookup takes O(1) average time.

# Space Complexity:- O(n)
# Extra space is used for the HashSet storing all elements.
