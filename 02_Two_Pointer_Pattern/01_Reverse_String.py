"""
LeetCode 344 — Reverse String

Key Idea:-
Use Recursion + Two Pointers.
    ->One pointer (l) starts from the beginning.
    ->Another pointer (r) starts from the end.
    ->Swap the characters at these positions.
    ->Recursively move both pointers toward the center.
    ->Stop when the pointers meet or cross.
Since the problem requires modifying the array in-place, no extra array is used.
"""
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse(l: int, r: int):
            # Continue until pointers cross
            if l < r:
                # Swap characters
                s[l], s[r] = s[r], s[l]
                # Move inward
                reverse(l + 1, r - 1)
        reverse(0, len(s) - 1)

"""
Time Complexity:    o(n)
Space complexity:   O(n)
"""
