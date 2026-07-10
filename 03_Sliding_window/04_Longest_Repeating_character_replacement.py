"""
Key Idea:-
    Use a Sliding Window + Frequency Hash Map.
    The goal is to find the longest substring that can be converted into a string of the same character by replacing at most k characters.

    Core Observation:-
        Suppose the current window has:
                                    Window Size = R - L + 1
                                    Maximum frequency of any character = maxFreq
    Then,
        Characters to Replace = Window Size - maxFreq
    If:
        (Window Size - maxFreq) <= k
            the current window is valid.
    Otherwise, shrink the window from the left.

Approach:-
    1.Initialize:
        A frequency dictionary count
        Left pointer L = 0
        maxFreq = 0
        result = 0
    2.Traverse the string using the right pointer.
    3.Update the frequency of the current character.
    4.Update the maximum frequency seen inside the current window.
    5.If:
        (window_size - maxFreq) > k
            shrink the window by moving L.
    6.Update the maximum valid window size.
    7.Return the result.
"""

from typing import Dict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Stores frequency of characters in the current window
        count = {}
        # Left pointer of the sliding window
        left = 0
        # Maximum frequency of a single character in the window
        maxFreq = 0
        # Length of the longest valid substring
        result = 0

        # Expand the window
        for right in range(len(s)):
            # Include current character
            count[s[right]] = 1 + count.get(s[right], 0)
            # Update highest frequency character
            maxFreq = max(maxFreq, count[s[right]])
            # If more than k replacements are needed,
            # shrink the window
            while (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            # Update answer
            result = max(result, right - left + 1)
        return result
"""
| Complexity       | Value              |
| ---------------- | ------------------ |
| Time Complexity  | O(n)               |
| Space Complexity | O(min(n, |Σ|))     |
"""
