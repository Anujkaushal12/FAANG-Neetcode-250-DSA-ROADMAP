"""
Leetcode question no: 238 :- product of array except  self

Key Idea:-
          For every index :- answer[i]=(product of left elements)×(product of right elements).

Instead of using division:
                         1. First pass → store left products.
                         2. Second pass → multiply with right products.

Approach:
# 1. Prefix Pass  -> Store product of all left elements
# 2. Postfix Pass -> Multiply with product of all right elements

This gives the answer in O(n) time.
"""

class Solution:
    def productExceptSelf(self, nums):
        res = [1] * len(nums)           # Initialize result array with 1

        prefix = 1                      # prefix stores product of elements on the left side
        for i in range(len(nums)):
            res[i] = prefix             # Store left product
            prefix *= nums[i]           # Update prefix

        postfix = 1                             # postfix stores product of elements on the right side
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= postfix                   # Multiply left product with right product
            postfix *= nums[j]                  # Update postfix
        return res


# ---------------- QUICK TEST ----------------
sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))     # Output: [24,12,8,6]
print(sol.productExceptSelf([-1,1,0,-3,3])) # Output: [0,0,9,0,0]


"""
Time Complexity:
The time complexity of this approach is O(n), where n is the number of elements in the input list. We perform two passes over the list to calculate the left and right products, and each pass takes O(n) time.

Space Complexity:
The space complexity is O(1) for the output list since we are allowed to return the result in the same list. Therefore, the space complexity is constant, as it does not depend on the size of the input list.
"""

