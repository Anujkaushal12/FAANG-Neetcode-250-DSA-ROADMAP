"""
Key Idea:-
    ->Use the Two Pointers technique.
    ->Traverse both strings simultaneously and alternately append one character from each string to the result. If one string is longer, append its remaining characters after the other string is exhausted.

Core Observation:-
    ->Maintain one pointer for each string.
    ->Append characters alternately.
    ->Continue until both strings are completely traversed.
Approach:-
    1.Initialize two pointers:
        l → points to word1
        r → points to word2
    2.Create an empty list res to store merged characters.
    3.While either string still has characters:
        If word1 has characters left, append one and move l.
        If word2 has characters left, append one and move r.
    4.Join the list into a string and return it.
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # Pointers for both strings
        l, r = 0, 0

        # Store merged characters
        res = []

        # Continue until both strings are completely processed
        while l < len(word1) or r < len(word2):

            # Add next character from word1 if available
            if l < len(word1):
                res.append(word1[l])
                l += 1

            # Add next character from word2 if available
            if r < len(word2):
                res.append(word2[r])
                r += 1

        # Convert list of characters into a string
        return "".join(res)
"""
| Complexity       | Value        |
| ---------------- | ------------ |
| Time Complexity  | **O(n + m)** |
| Space Complexity | **O(n + m)** |

"""