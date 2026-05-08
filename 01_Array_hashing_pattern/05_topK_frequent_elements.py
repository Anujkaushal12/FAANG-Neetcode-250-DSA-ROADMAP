"""
LeetCode 347 — Top K Frequent Elements

Key Idea
->Use a frequency hashmap to count how many times each number appears, then use Bucket Sort to group numbers by their frequencies.
->Since the maximum possible frequency of any number is len(nums), we create buckets where:
->freq[i] stores all numbers appearing exactly i times.
->Then traverse buckets from highest frequency to lowest and collect the first k elements.

Approach
1. Create a dictionary count to store frequency of each number.
2. Create a bucket list freq where index represents frequency.
3. Store numbers into their corresponding frequency bucket.
4. Traverse buckets in reverse order (highest frequency first).
5. Add elements into result until k elements are collected.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to store frequency of each number
        count = {}

        # Bucket list where index = frequency
        # Example: freq[2] contains numbers that are appearing 2 times
        freq = [[] for i in range(len(nums) + 1)]

        # Count frequency of each element
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # Place numbers into their frequency bucket
        for n, c in count.items():
            freq[c].append(n)
        
        # Result list
        res = []
        # Traverse from highest frequency to lowest
        for x in range(len(freq) - 1, 0, -1):
            # Add all numbers from current bucket
            for y in freq[x]:
                res.append(y)
                # Return once k elements are collected
                if len(res) == k:
                    return res

# Quick Test

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))        # Output: [1, 2]
print(sol.topKFrequent([1], 1))                  # Output: [1]
print(sol.topKFrequent([4,4,4,6,6,1,1,1,1], 2))  # Output: [1, 4]

"""
Time Complexity:
The time complexity of this approach is O(n + k*log(n)), where n is the number of elements in the input list. Building the frequency map takes O(n) time, and inserting k elements into the min-heap takes O(k*log(n)) time.

Space Complexity:
The space complexity is O(n) because we need to store the frequency map of all elements in the input list. Additionally, the min-heap will also have a space complexity of O(n) in the worst case if all elements are unique.
"""

        