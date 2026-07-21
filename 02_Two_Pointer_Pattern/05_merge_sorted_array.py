"""
Key Idea

Use the Two Pointers technique by merging the arrays from the end.

Since nums1 already has enough extra space to hold all elements of nums2, filling the array from the back prevents overwriting the existing elements in nums1.

Core Observation
The largest element is always at the end of either nums1 or nums2.
Place the larger element at the last available position.
Move the corresponding pointer backward.
Continue until all elements are merged.

Approach:-
    1.Initialize three pointers:
        m - 1 → last valid element in nums1
        n - 1 → last element in nums2
        last → last index of nums1
    2.Compare the last elements of both arrays.
    3.Place the larger element at nums1[last].
    4.Move the corresponding pointer backward.
    5.Repeat until one array is exhausted.
    6.If elements remain in nums2, copy them into nums1.
    7.No need to copy remaining elements of nums1 since they are already in the correct position.
"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int,
              nums2: List[int], n: int) -> None:

        # Pointer to the last position in nums1
        last = m + n - 1

        # Merge both arrays from the end
        while m > 0 and n > 0:

            # Compare the largest remaining elements
            if nums1[m - 1] > nums2[n - 1]:
                # Place larger element at the end
                nums1[last] = nums1[m - 1]
                m -= 1

            else:
                # Place larger element from nums2
                nums1[last] = nums2[n - 1]
                n -= 1

            # Move to the next position
            last -= 1

        # Copy remaining elements of nums2 (if any)
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1

"""
| Complexity       | Value        |
| ---------------- | ------------ |
| Time Complexity  |   O(m + n)   |
| Space Complexity |   O(1)       |

"""