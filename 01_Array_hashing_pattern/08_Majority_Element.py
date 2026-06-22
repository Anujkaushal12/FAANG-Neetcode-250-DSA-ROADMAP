#LeetCode 169 — Majority Element

"""
Key Idea:-
    Use the Boyer-Moore Voting Algorithm.

    The majority element appears more than n/2 times, so even if we cancel out one occurrence of the majority element with one occurrence of a different element, the majority element will still remain.

The algorithm:
    Maintains a candidate (res)
    Maintains a vote count (count)
    If count becomes 0, choose the current element as the new candidate.
    Increase count if the current element matches the candidate.
    Otherwise, decrease count.

At the end, the candidate is guaranteed to be the majority element.

Approach:-
    Initialize:
    res = 0 (candidate)
    count = 0 (vote count)
    Traverse the array.
    If count == 0, set the current number as the candidate.
    If the current number equals the candidate:
    Increment count
    Otherwise:
        Decrement count
        Return the candidate.

Since the problem guarantees that a majority element exists, the final candidate is the answer.
"""

from typing import List

class Solution:
    def majorityelemnt(self,nums: List[int])-> int:
        res,count=0,0
        for n in nums:
            if count==0:
                res=n
            count += (1 if n==res else -1)
        return res

"""
Complexity Analysis
Time Complexity	    -->     O(n)
Space Complexity	-->     O(1)
"""