"""
LeetCode #49 - Group Anagrams

🔑 KEY IDEA
Two strings are anagrams if they have the EXACT same character
frequency.we build a fixed-size frequency array of length 26 
(one slot per a–z).This array, converted to a tuple, becomes 
a hashable key that groups all anagrams together in a dictionary.

Core insight: anagram ↔ identical character-count signature.

 APPROACH — Character Count Hashing
 --------------------------
 1. Create a defaultdict(list) so any unseen key auto-initialises
    to an empty list — no KeyError, no manual `.setdefault()`.

 2. For every string, build a count array of size 26.
    count[0] = freq of 'a', count[1] = freq of 'b', …
    Use `ord(c) - ord('a')` to map each character to an index.

 3. Convert the list → tuple (lists are mutable, so unhashable;
    tuples are immutable and can be used as dict keys).

 4. Append the original string under that tuple key.
    Anagrams produce identical tuples → land in the same bucket.

 5. Return all value-lists from the dict.

 Commone Mistakes or pitfalls:
 ✗  Using a plain dict  → KeyError on first unseen key
 ✗  count[ord("c") - ord("a")]  → indexes on the letter "c", not
    the loop variable c  (subtle but breaks everything)
 ✗  res[count].append(s)  → TypeError: unhashable type 'list'
    Fix: res[tuple(count)].append(s)
"""

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Each unique frequency-tuple maps to a list of anagram strings
        res = defaultdict(list)
        for s in strs:
            # Frequency array: index 0 → 'a', index 25 → 'z'
            count = [0] * 26
            for c in s:
                # c is the loop variable (current character), NOT the string literal "c" — a common source of bugs
                count[ord(c) - ord("a")] += 1
            # tuple() makes the list hashable so it can serve as a dict key
            res[tuple(count)].append(s)
        # .values() gives all anagram groups; wrap in list() for the return type
        return list(res.values())

# Quick Test
sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# Complexity (Time and Space)
# Time : O(n * k)  — n = number of strings, k = max string length
#                    (vs O(n * k log k) for the sorting approach)
# Space: O(n * k)  — storing all strings in the hash map