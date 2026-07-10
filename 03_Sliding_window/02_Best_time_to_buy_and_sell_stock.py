"""
Key Idea:-
    Use the Two Pointers technique.

The goal is to maximize:
                    Profit = Selling Price - Buying Price

To achieve the maximum profit:
    Keep track of the lowest buying price seen so far.
    For every new price, treat it as a potential selling price.
    Calculate the profit and update the maximum profit if it is larger.
    If a lower buying price is found, update the buying pointer.

Approach:-
    Initialize:
        left → Buy day.
        right → Sell day.
        maxProfit = 0.
    Traverse the array with the right pointer.
    If:
        prices[left] < prices[right]
    calculate the profit and update the maximum profit.
    Otherwise:
        Move left to right because a lower buying price has been found.
    Continue until the end of the array.
    Return the maximum profit.
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Maximum profit found so far
        maxProfit = 0
        # Left pointer -> Buy day
        left = 0
        # Right pointer -> Sell day
        right = 1

        # Traverse the array
        while right < len(prices):
            # Profitable transaction
            if prices[left] < prices[right]:
                # Calculate current profit
                profit = prices[right] - prices[left]
                # Update maximum profit
                maxProfit = max(maxProfit, profit)
            else:
                # Found a lower buying price
                left = right
            # Move to the next day
            right += 1
        return maxProfit
"""
Complexity	Value
Time Complexity	    -->     O(n)
Space Complexity	-->     O(1)
"""