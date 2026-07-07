"""
Key Idea:-
    ->Use Binary Search on the Window.
    ->Instead of searching for individual elements, search for the starting index of the window of size k.

Core Observation:-
    ->The answer is always a contiguous subarray of length k because the array is sorted.
    ->Suppose the window starts at index mid.
    ->There are two possible windows:
        Window 1: arr[mid : mid + k]
        Window 2: arr[mid + 1 : mid + k + 1]
    ->Compare which window is closer to x.
        ->If:
            x - arr[mid] > arr[mid + k] - x, then the right window is better.
        ->Otherwise, the left window is better.

Approach:-
    1.The window can start anywhere from:  
            ->0
            ->len(arr) - k
    2.Perform binary search on these possible starting positions.
    3.At each midpoint:
            Compare the distance of the left boundary and the element just outside the right boundary.
            Move left or right accordingly.
    4.After binary search, left will be the optimal starting index.
    5.Return the subarray of length k.
"""
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Possible starting positions of the window
        left = 0
        right = len(arr) - k

        # Binary search for the best window
        while left < right:
            mid = (left + right) // 2

            # Compare which window is closer to x
            if x - arr[mid] > arr[mid + k] - x:
                # Better window starts to the right
                left = mid + 1

            else:
                # Better window starts at mid or before
                right = mid

        # Return the k closest elements
        return arr[left:left + k]
"""
| Complexity       | Value                                  |
| ---------------- | -------------------------------------- |
| Time Complexity  | O(log(n - k) + k)                      |
| Space Complexity | O(1)** *(excluding the output list)    |
"""
