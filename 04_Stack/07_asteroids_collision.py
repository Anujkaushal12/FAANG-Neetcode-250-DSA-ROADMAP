"""
LeetCode 735. Asteroid Collision

Key Idea:-
    Use a stack to simulate the movement of asteroids.
        Positive values move right.
        Negative values move left.
        A collision can only occur when a right-moving asteroid is already on the stack and the current asteroid is moving left.
        Resolve collisions until one asteroid survives or both explode.

Approach:-
    1.Initialize an empty stack.
    2.Traverse each asteroid:
        ->If the current asteroid is moving left (< 0) and the top of the stack is moving right (> 0), a collision occurs.
        ->Compare their sizes:
            If the current asteroid is larger, remove the top asteroid and continue checking for more collisions.
            If the top asteroid is larger, destroy the current asteroid.
            If both have the same size, destroy both.
    3.If the current asteroid survives all collisions, push it onto the stack.
    4.After processing all asteroids, the stack contains the final state.
"""
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Stack to store asteroids that survive so far
        stack = []

        # Process each asteroid
        for asteroid in asteroids:

            # Resolve collisions while:
            # - there is a right-moving asteroid on the stack
            # - the current asteroid is moving left
            while stack and asteroid < 0 and stack[-1] > 0:

                # Compare their sizes
                diff = asteroid + stack[-1]

                if diff < 0:
                    # Current asteroid is larger
                    # Destroy the top asteroid and continue checking
                    stack.pop()

                elif diff > 0:
                    # Stack asteroid is larger
                    # Current asteroid is destroyed
                    asteroid = 0

                else:
                    # Both asteroids have equal size
                    # Destroy both
                    asteroid = 0
                    stack.pop()

            # Push the asteroid if it survived
            if asteroid:
                stack.append(asteroid)

        return stack

"""
Time Complexity:-
                O(n)
Space Complexity:-
                O(n)
"""
