"""
LeetCode 84. Largest Rectangle in Histogram

Key Idea:-
    Use a Monotonic Increasing Stack to efficiently determine the maximum rectangle area.
    The stack stores (start_index, height) pairs in increasing height order.
    When a shorter bar is encountered, taller bars can no longer extend further, so compute their maximum possible rectangle areas.
    After processing all bars, calculate the remaining areas for bars still in the stack.
Approach:-
    1.Initialize an empty stack and a variable to store the maximum area.
    2.Traverse each histogram bar:
        Keep track of the current bar's starting index.
        While the current height is smaller than the stack's top height:
            Pop the taller bar.
            Calculate its rectangle area using:
                Height = popped bar's height.
                Width = current index − popped bar's starting index.
            Update the maximum area.
            Update the current starting index so the shorter bar can extend left.
        Push the current (start_index, height) onto the stack.
    3.After traversing the histogram:
        Compute the area for every remaining bar using the histogram's end as the right boundary.
    4.Return the maximum rectangle area found.
"""
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Monotonic increasing stack
        # Stores (start_index, height)
        stack = []

        # Stores the maximum rectangle area
        maxArea = 0

        # Traverse every histogram bar
        for i, h in enumerate(heights):
            start = i

            # Current bar is shorter, so taller bars end here
            while stack and stack[-1][1] > h:
                index, height = stack.pop()

                # Calculate the rectangle area
                maxArea = max(maxArea, height * (i - index))

                # Extend the current bar to the popped bar's start
                start = index

            # Store the earliest possible start for this height
            stack.append((start, h))

        # Compute areas for bars extending to the end
        for index, height in stack:
            maxArea = max(maxArea, height * (len(heights) - index))

        return maxArea

"""
Time Complexity:-
                O(n)
Space Complexity:-
                O(n)
"""