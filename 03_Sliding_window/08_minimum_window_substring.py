"""
Key Idea:-
    Use a Sliding Window + Hash Map.
    Instead of checking every substring, maintain a window that expands until it contains all characters of t, then shrink it as much as possible while still satisfying the requirement.

Optimization:-
    Before applying the sliding window, filter the string s to keep only characters that appear in t.
    This avoids processing irrelevant characters and improves efficiency.

Approach:-
    1.Count the frequency of every character in t.
    2.Filter s to include only characters that exist in t, along with their indices.
    3.Use two pointers (left and right) to maintain a sliding window over the filtered list.
    4.Expand the window until all required characters are included.
    5.Shrink the window to find the smallest valid substring.
    6.Keep track of the smallest valid window.
    7.Return the substring corresponding to the smallest window.
"""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Edge case
        if not t or not s:
            return ""

        # Count frequency of each character in t
        dict_t = Counter(t)

        # Number of unique characters required
        required = len(dict_t)

        # Filter s to keep only relevant characters
        filtered_s = []

        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))

        # Sliding window pointers
        left = 0
        right = 0

        # Number of characters currently satisfying required frequency
        formed = 0

        # Current window character counts
        window_counts = {}

        # Store best answer
        # (window_length, start_index, end_index)
        ans = (float("inf"), None, None)

        # Expand window
        while right < len(filtered_s):

            character = filtered_s[right][1]

            # Add current character
            window_counts[character] = window_counts.get(character, 0) + 1

            # Required frequency achieved
            if window_counts[character] == dict_t[character]:
                formed += 1

            # Contract window while valid
            while left <= right and formed == required:

                character = filtered_s[left][1]

                start = filtered_s[left][0]
                end = filtered_s[right][0]

                # Update smallest window
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                # Remove left character
                window_counts[character] -= 1

                # Window no longer valid
                if window_counts[character] < dict_t[character]:
                    formed -= 1

                left += 1

            # Expand window
            right += 1

        # Return answer
        if ans[0] == float("inf"):
            return ""

        return s[ans[1]: ans[2] + 1]
"""
| Complexity       | Value                   |
| ---------------- | ----- | - | - | - | --- |
| Time Complexity  | **O(  | S | + | T | )** |
| Space Complexity | **O(  | S | + | T | )** |
"""
