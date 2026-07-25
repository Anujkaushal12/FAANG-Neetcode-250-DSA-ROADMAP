"""
LeetCode 682 — Baseball Game

Key Idea:-
    ->Use a Stack to keep track of valid scores.
    ->Each operation modifies the previous scores according to the given rules:
        Integer → Add a new score.
        "+"  Sum of the last two valid scores.
        "D" → Double the last valid score.
        "C" → Remove the last valid score.
    ->The stack naturally supports accessing and modifying the most recent scores efficiently.

Approach:-
    1.Create an empty stack.
    2.Traverse each operation in ops.
    3.Process based on the operation:
        "+" → Push the sum of the last two scores.
        "D" → Push twice the last score.
        "C" → Remove the last score.
        Otherwise → Convert the string to an integer and push it.
    4.Return the sum of all values remaining in the stack.
"""

from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        # Stack to store valid scores
        stack = []

        # Process each operation
        for op in ops:
            # Sum of previous two scores
            if op == "+":
                stack.append(stack[-1] + stack[-2])

            # Remove previous score
            elif op == "C":
                stack.pop()

            # Double previous score
            elif op == "D":
                stack.append(2 * stack[-1])

            # New integer score
            else:
                stack.append(int(op))

        # Total score
        return sum(stack)

"""
| Complexity       | Value    |
| ---------------- | -------- |
| Time Complexity  | **O(n)** |
| Space Complexity | **O(n)** |
"""
