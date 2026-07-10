"""
Key Idea:-
    ->Use a Monotonic Deque (Decreasing Queue).
    ->The goal is to find the maximum element in every window of size k.
Core Observation:-
    ->A normal sliding window cannot efficiently find the maximum after each shift.
    ->Instead, maintain a deque that stores indices of elements in decreasing order of their values.
    ->The deque always satisfies:
        The front contains the maximum element of the current window.
        Elements smaller than the current element are removed from the back because they can never become the maximum in future windows.

Approach:-
    1.Initialize:
        ->An empty deque to store indices.
        ->Two pointers left and right.
        ->An output list.
    2.Expand the window by moving right.
    3.Remove all smaller elements from the back of the deque.
    4.Add the current index to the deque.
    5.Remove the front index if it is outside the current window.
    6.Once the window size reaches k:
        ->The front of the deque is the maximum.
        ->Add it to the answer.
        ->Move the left pointer.
    7.Continue until the end of the array.
"""

from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Stores the maximum of each window
        output = []
        # Monotonic decreasing deque (stores indices)
        deque = collections.deque()
        # Sliding window pointers
        left = 0
        right = 0

        # Traverse the array
        while right < len(nums):

            # Remove all smaller elements from the back
            # because they can never become the maximum
            while deque and nums[deque[-1]] < nums[right]:
                deque.pop()

            # Add current index
            deque.append(right)

            # Remove indices that are outside the current window
            if left > deque[0]:
                deque.popleft()

            # Window has reached size k
            if (right + 1) >= k:
                # Front of deque contains maximum element
                output.append(nums[deque[0]])
                # Slide the window
                left += 1
            right += 1

        return output

"""
| Complexity       | Value    |
| ---------------- | -------- |
| Time Complexity  | O(n)     |
| Space Complexity | O(k)     |
"""