"""
LeetCode 901. Online Stock Span

Key Idea:-
    Use a Monotonic Decreasing Stack to efficiently compute the stock span.
        ->The stack stores (price, span) pairs.
        ->For each new stock price:
            Remove all previous prices that are less than or equal to the current price.
            Accumulate their spans into the current span.
            Push the current (price, span) onto the stack.
        ->This avoids repeatedly checking previous prices, giving an efficient O(1) amortized solution.

Approach:-
    1.Initialize an empty stack that stores (price, span) pairs.
    2.For every new stock price:
        ->Start with a span of 1 (the current day).
        ->While the stack is not empty and the top price is less than or equal to the current price:
            Add the stored span to the current span.
            Remove that price from the stack.
        ->Push the current (price, span) onto the stack.
        Return the computed span.
    3.Since each price is pushed and popped at most once, the solution is efficient.
"""
class StockSpanner:

    def __init__(self):
        # Monotonic decreasing stack
        # Stores (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        # Every new price has at least a span of 1
        span = 1

        # Merge spans of previous prices that are
        # less than or equal to the current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()

        # Store the current price along with its computed span
        self.stack.append((price, span))

        # Return today's stock span
        return span

"""
Time Complexity:-
| Operation  | Complexity         |
| ---------- | ------------------ |
| **next()** | **O(1) amortized** |

Space Complexity:-
                O(n)
"""