"""
Key Idea:-
    Use a Sliding Window + Hash Set.
    ->Maintain a window [left, right] that always contains unique characters.
    ->Expand the window by moving right.
    ->If a duplicate appears, shrink the window from the left until the duplicate is removed.
    ->Track the maximum window size seen so far.
This avoids checking every substring and achieves O(n) time.

Approach:-
    1.Initialize an empty set charset to store characters currently in the window.
    2.Set left = 0 and maxLength = 0.
    3.For each right index:
        ->If s[right] is not in the set, add it and update maxLength.
        ->Otherwise, repeatedly remove characters from the left side until s[right] is no longer in the set.
        ->Add s[right] back into the set.
    4.Return maxLength.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Stores unique characters in current window
        charSet = set()
        # Left pointer of sliding window
        left = 0
        # Length of longest valid substring
        maxLength = 0

        # Expand window using right pointer
        for right in range(len(s)):
            # If duplicate character exists
            while s[right] in charSet:
                # Remove leftmost character
                charSet.remove(s[left])
                # Shrink window
                left += 1
            # Add current character
            charSet.add(s[right])
            # Update answer
            maxLength = max(maxLength, right - left + 1)
        return maxLength
"""
Complexity              Value
Time Complexity    -->  O(n)

Space Complexity    --> O(min(n, |Σ|))
"""