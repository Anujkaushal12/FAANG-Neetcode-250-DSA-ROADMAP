"""
LeetCode 853. Car Fleet

Key Idea:-
    Sort the cars by their starting position (closest to the target processed first) and use a stack to track the arrival time of each fleet.
        ->Each car's arrival time is calculated as:
                                                    time=(target - position)/speed
        ->If a car behind reaches the target earlier than or at the same time as the fleet ahead, it catches up and becomes part of that fleet.
        ->Otherwise, it forms a new fleet.

Approach:-
    1.Pair each car's position with its speed.
    2.Sort the cars by position in ascending order.
    3.Traverse the sorted cars from right to left (closest to the target first).
    4.For each car:
        ->Compute its time to reach the target.
        ->Push the time onto the stack.
        ->If the current car's arrival time is less than or equal to the fleet ahead, merge them by removing the current time from the stack.
    5.The number of remaining times in the stack equals the number of car fleets.
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's position with its speed
        pair = [[p, s] for p, s in zip(position, speed)]

        # Stack stores the arrival time of each fleet
        stack = []

        # Process cars from closest to the target to farthest
        for p, s in sorted(pair)[::-1]:

            # Calculate the time needed to reach the target
            arrival_time = (target - p) / s
            stack.append(arrival_time)

            # If the current car catches the fleet ahead,
            # merge them into one fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        # Number of fleets equals the number of remaining arrival times
        return len(stack)
"""
Time Complexity:-
                O(n log n)
Space Complexity:-
                O(n)
"""