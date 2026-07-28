"""
LeetCode 394. Decode String

Key Idea:-
    ->Use a stack to decode nested encoded strings.
        Push characters onto the stack until a closing bracket ']' is encountered.
        When ']' is found:
            Extract the encoded substring until '['.
            Extract the repetition count (which may contain multiple digits).
            Repeat the substring k times and push the decoded result back onto the stack.
        Continue until the entire string is processed.

Approach:-
    1.Initialize an empty stack.
    2.Traverse each character in the input string:
        ->If the character is not ']', push it onto the stack.
        ->Otherwise:
            Pop characters until '[' to build the encoded substring.
            Remove '['.
            Pop all consecutive digits to determine the repetition count.
            Repeat the substring k times.
            Push the decoded string back onto the stack.
    3.After processing all characters, join the stack to obtain the fully decoded string.
"""
class Solution:
    def decodeString(self, s: str) -> str:
        # Stack to store characters and decoded substrings
        stack = []

        # Traverse each character
        for ch in s:

            # Push everything except the closing bracket
            if ch != "]":
                stack.append(ch)

            else:
                # Build the substring inside the brackets
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr

                # Remove the opening bracket
                stack.pop()

                # Build the repetition count (handles multiple digits)
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                # Push the expanded substring back onto the stack
                stack.append(int(k) * substr)

        # Join all decoded parts
        return "".join(stack)

"""
Time Complexity:-
                O(n)
Space Complexity:-
                O(n)
"""