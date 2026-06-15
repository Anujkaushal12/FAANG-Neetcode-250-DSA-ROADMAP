"""
LeetCode 14 — Longest Common Prefix

Key Idea:-
    ->Use the first string as a reference and compare its characters with the corresponding characters in all other strings.

    ->For each character position:
        Check whether every string has the same character at that index.
        If any string is shorter or contains a different character, the current prefix is the longest common prefix.
        Otherwise, add the character to the result and continue.

->Approach:-
    1.Initialize an empty string res to store the common prefix.
    2.Iterate through each character index of the first string.
    3.For each index, compare the character with the character at the same position in every other string.
    4.If:
        The current index is out of bounds for any string, or
        The character does not match,
    return the current prefix stored in res.
    5.If all strings match at the current index, append the character to res.
    6.After checking all characters, return res.
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Store the longest common prefix
        res = ""
        # Iterate through each character of the first string
        for i in range(len(strs[0])):
            # Compare with every string
            for s in strs:
                # If index is out of range or characters don't match
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            # Add matching character to the prefix
            res += strs[0][i]
        return res

# Complexity Analysis

# Time Complexity: O(n × m)

# Space Complexity: O(1) (excluding the output string)