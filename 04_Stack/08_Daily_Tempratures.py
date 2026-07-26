"""
LeetCode 739. Daily Temperatures

Key Idea:-
    ->Use a Monotonic Decreasing Stack to keep track of temperatures whose next warmer day has not been found yet.
        The stack stores (temperature, index) pairs.
        When a warmer temperature is encountered, repeatedly pop colder temperatures from the stack and calculate how many days they had to wait.
        Any temperatures left in the stack do not have a warmer future day, so their answer remains 0.

Approach:-
    1.Initialize a result array res with all values set to 0.
    2.Maintain a stack storing (temperature, index) pairs in decreasing temperature order.
    3.Traverse the temperature array:
        ->While the current temperature is greater than the temperature at the top of the stack:
            Pop the stack.
            Calculate the number of days waited as current_index - previous_index.
            Store the result in res.
        ->Push the current (temperature, index) onto the stack.
    4.Return the result array.
"""
from typing import List

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        # Initialize the result array with 0s
        # Default value 0 means no warmer day exists
        res = [0] * len(temp)

        # Monotonic decreasing stack
        # Stores [temperature, index]
        stack = []

        # Traverse each day's temperature
        for i, t in enumerate(temp):

            # Current temperature is warmer than previous unresolved days
            while stack and t > stack[-1][0]:
                prevTemp, prevIndex = stack.pop()

                # Calculate the number of days waited
                res[prevIndex] = i - prevIndex

            # Store the current temperature and its index
            stack.append([t, i])

        return res

"""
Time Complexity:-
                O(n)
Space Complexity:-
                O(n)
"""