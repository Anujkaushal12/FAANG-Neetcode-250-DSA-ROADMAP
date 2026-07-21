"""
Key Idea:-
    Use the Two Pointers technique.
    Traverse the string from both ends while ignoring non-alphanumeric characters and comparing characters case-insensitively.

Core Observation:-
    Skip characters that are not letters or digits.
    Convert both characters to lowercase before comparing.
    If all valid characters match, the string is a palindrome.

Approach:-
    1.Initialize two pointers:
        left at the beginning.
        right at the end.
    2.Move left forward until it points to an alphanumeric character.
    3.Move right backward until it points to an alphanumeric character.
    4.Compare the lowercase versions of both characters.
    5.If they differ, return False.
    6.Otherwise, move both pointers inward.
    7.Continue until the pointers meet.
    8.Return True.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Two pointers
        l, r = 0, len(s) - 1

        while l < r:

            # Skip non-alphanumeric characters from the left
            while l < r and not self.alphaNum(s[l]):
                l += 1

            # Skip non-alphanumeric characters from the right
            while r > l and not self.alphaNum(s[r]):
                r -= 1

            # Compare characters (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False

            # Move both pointers
            l += 1
            r -= 1

        # String is a palindrome
        return True

    # Check whether a character is alphanumeric
    def alphaNum(self, c: str) -> bool:
        return (
            ord("A") <= ord(c) <= ord("Z") or
            ord("a") <= ord(c) <= ord("z") or
            ord("0") <= ord(c) <= ord("9")
        )

"""
| Complexity       | Value    |
| ---------------- | -------- |
| Time Complexity  | **O(n)** |
| Space Complexity | **O(1)** |
"""