"""
Key Idea:-
Use a Greedy + Two Pointers approach.
    ->Sort the array so the lightest and heaviest people can be easily accessed.  
    ->Always place the heaviest person in a boat.
    ->Try to pair them with the lightest remaining person.
    ->If they fit within the weight limit, both share one boat.
    ->Otherwise, the heaviest person goes alone.
This greedy strategy guarantees the minimum number of boats.

Approach:-
    1.Sort the people array.
    2.Initialize two pointers:
        l → Lightest person.
        r → Heaviest person.
    3.While l <= r:
        ->Reserve one boat for the heaviest person.
        ->Calculate the remaining capacity.
        ->If the lightest person fits, place them in the same boat.
        ->Move pointers accordingly.
    4.Return the total number of boats.
"""

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # Sort the people by weight
        people.sort()

        # Number of boats used
        boats = 0

        # Two pointers
        left = 0                      # Lightest person
        right = len(people) - 1       # Heaviest person

        # Continue until everyone is assigned a boat
        while left <= right:

            # Remaining capacity after taking the heaviest person
            remaining = limit - people[right]

            # Heaviest person boards the boat
            right -= 1

            # One boat is used
            boats += 1

            # If the lightest person can fit, pair them together
            if left <= right and people[left] <= remaining:
                left += 1

        return boats

"""
Complexity Analysis
Time Complexity	    -->     O(n log n)
Space Complexity	-->     O(1) (excluding sorting space)
"""