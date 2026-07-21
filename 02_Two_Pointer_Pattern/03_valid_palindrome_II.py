"""
Key Idea:-
    Use the Two Pointers technique.
    Traverse the string from both ends. If a mismatch occurs, try deleting either the left character or the right character exactly once. If either resulting substring is a palindrome, return True.

Core Observation:-
    At the first mismatch:
        Skip the left character and check if the remaining substring is a palindrome.
        Skip the right character and check if the remaining substring is a palindrome.  
    If either check succeeds, the original string can become a palindrome after deleting at most one character.

    Approach:-
    Initialize two pointers:
    left at the beginning.
    right at the end.
    Compare characters while moving inward.
    If characters match:
    Move both pointers.
    If a mismatch occurs:
    Create two substrings:
    Skip the left character.
    Skip the right character.
    Check whether either substring is a palindrome.
    If no mismatches occur, return True.
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Two pointers at both ends
        l, r = 0, len(s) - 1
        # Compare characters
        while l < r:
            # Mismatch found
            if s[l] != s[r]:
                # Skip left character
                skipL = s[l + 1 : r + 1]
                # Skip right character
                skipR = s[l : r]
                # If either substring is a palindrome
                return (
                    skipL == skipL[::-1] or
                    skipR == skipR[::-1]
                )
            # Move both pointers
            l += 1
            r -= 1
        # Already a palindrome
        return True

"""
| Complexity       | Value    |
| ---------------- | -------- |
| Time Complexity  | O(n)     |
| Space Complexity | O(n)     |
"""