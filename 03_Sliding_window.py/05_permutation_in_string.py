"""
Key Idea:-
    Use a Sliding Window + Frequency Counting.
    
    A permutation of s1 exists in s2 if a substring of length len(s1) has exactly the same character frequencies.

    Instead of sorting every substring (O(n log n)), compare frequency arrays.

    Core Observation:-
        Two strings are permutations if:
            Character frequencies are identical.
        Since the strings contain only lowercase English letters, use two arrays of size 26.

Approach:-
    1.If len(s1) > len(s2), return False.
    2.Build frequency arrays for:
        s1
        First window of s2
    3.Count how many of the 26 characters have matching frequencies.
    4.Slide the window:
        Add the new character.
        Remove the leftmost character.
        Update the number of matching frequencies.
    5.If all 26 frequencies match, return True.
    6.Otherwise return False.
"""

from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer, permutation is impossible
        if len(s1) > len(s2):
            return False

        # Frequency arrays for s1 and current window of s2
        s1Count = [0] * 26
        s2Count = [0] * 26

        # Build frequency arrays
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        # Count matching frequencies
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        left = 0
        # Slide the window
        for right in range(len(s1), len(s2)):
            # All frequencies match
            if matches == 26:
                return True
            
            # Add new character
            index = ord(s2[right]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Remove leftmost character
            index = ord(s2[left]) - ord("a")
            s2Count[index] -= 1

            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            left += 1

        return matches == 26
            
"""
| Complexity       | Value    |
| ---------------- | -------- |
| Time Complexity  | O(n)     |
| Space Complexity | O(1)     |

"""