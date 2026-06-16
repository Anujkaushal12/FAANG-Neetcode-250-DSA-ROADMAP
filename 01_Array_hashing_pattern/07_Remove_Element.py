"""
LeetCode#27 - Remove Element

Key Idea:-
->Use a two-pointer approach:
    1.Pointer i traverses the entire array.
    2.Pointer k keeps track of the position where the next valid element should be placed.
    3.Whenever an element is not equal to val, copy it to index k and increment k.
    4.After processing all elements, the first k elements of the array contain the required result.

Approach:-
    1.Initialize k = 0.
    2.Traverse the array using index i.
    3.If nums[i] != val:
        (i)Place nums[i] at nums[k].
        (ii)Increment k.
    4.Return k.

->The first k elements of nums represent the array after removing all occurrences of val.
"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer to track the position of valid elements
        k = 0
        # Traverse the array
        for i in range(len(nums)):
            # If current element is not equal to val
            if nums[i] != val:
                # Place it at the next valid position
                nums[k] = nums[i]
                # Move valid position pointer forward
                k += 1
        # Return count of valid elements
        return k
    
"""
Complexity Analysis:-
    Time Complexity	   -->  O(n)
    Space Complexity   -->  O(1)
"""