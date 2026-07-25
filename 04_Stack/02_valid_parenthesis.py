"""
LeetCode 20. Valid Parentheses

Key Idea:-
    Use a stack to keep track of opening brackets. Whenever a closing bracket is encountered, check whether it matches the most recent opening bracket. If it does, remove the opening bracket from the stack; otherwise, the string is invalid.

Approach:-
    1.Create an empty stack to store opening brackets.
    2.Create a dictionary that maps each closing bracket to its corresponding opening bracket.
    3.Traverse each character in the string:
        ->If it is a closing bracket:
            Check if the stack is not empty and the top of the stack matches the expected opening bracket.
            If it matches, pop the stack.
            Otherwise, return False.
        ->If it is an opening bracket, push it onto the stack.
    4.After processing all characters:
        ->If the stack is empty, all brackets were matched correctly.
        ->Otherwise, return False.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to store opening brackets
        stack = []

        # Mapping of closing brackets to their corresponding opening brackets
        closeToOpen = {")": "(","]": "[","}": "{"}

        # Traverse each character in the string
        for c in s:
            # If current character is a closing bracket
            if c in closeToOpen:
                # Check whether the top of the stack matches
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()  # Remove the matched opening bracket
                else:
                    return False  # Mismatched or missing opening bracket
            else:
                # Opening bracket -> push onto the stack
                stack.append(c)

        # Valid only if no unmatched opening brackets remain
        return len(stack) == 0

"""
Time Complexity:-   
                O(n)
Space Complexity:-
                O(n)
"""