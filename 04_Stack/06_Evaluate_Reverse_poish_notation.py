"""
LeetCode 150. Evaluate Reverse Polish Notation

Key Idea:-
    Use a stack to evaluate the expression from left to right.
    Push operands (numbers) onto the stack.
    When an operator is encountered, pop the required operands, perform the operation, and push the result back onto the stack.
    After processing all tokens, the remaining element in the stack is the final answer.

Approach:-
    1.Initialize an empty stack.
    2.Traverse each token in the input:
        ->If the token is a number, convert it to an integer and push it onto the stack.
        ->If the token is an operator (+, -, *, /):
            Pop the top two operands from the stack.
            Perform the operation in the correct order (second_operand operator first_operand).
            Push the result back onto the stack.
    3.After processing all tokens, return the only remaining element in the stack.
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Stack to store operands
        stack = []

        # Traverse each token
        for token in tokens:

            # Addition
            if token == "+":
                stack.append(stack.pop() + stack.pop())

            # Subtraction (order matters)
            elif token == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)

            # Multiplication
            elif token == "*":
                stack.append(stack.pop() * stack.pop())

            # Division (truncate toward zero)
            elif token == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second / first))

            # Operand -> push onto the stack
            else:
                stack.append(int(token))

        # Final result
        return stack[0]
"""
Time Complexity:-
                O(n)
Space Complexity:-
                O(n)
"""