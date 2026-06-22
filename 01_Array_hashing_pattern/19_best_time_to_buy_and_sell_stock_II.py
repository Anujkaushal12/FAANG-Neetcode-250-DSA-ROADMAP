"""
LeetCode 122 — Best Time to Buy and Sell Stock II

Key Idea:-
    Use a Greedy Approach.
    Whenever the stock price increases from one day to the next, we can capture that profit.
    Instead of trying to find the absolute lowest buy point and highest sell point, simply take every positive price difference.

Approach:-
    Initialize profit = 0.
    Traverse the array from index 1.
    If today's price is greater than yesterday's price:
    Add the difference to profit.
    Return the total profit.

This works because every profitable upward movement contributes to the final maximum profit.
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Stores total profit
        profit = 0

        # Traverse the array
        for i in range(1, len(prices)):

            # If price increased, capture the profit
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit

"""
Complexity Analysis

Time Complexity	 :-     O(n)
Space Complexity :- 	O(1)
"""