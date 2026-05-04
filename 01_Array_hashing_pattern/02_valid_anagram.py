"""
Problem: LeetCode 242 - Valid Anagram 

Key Insights:

Edge Case: Different lengths: Always check length first; if len(s) != len(t), they cannot be anagrams.

Detailed Approach: Frequency Counter (Hash Map/Array)
1.Why: An anagram means both strings have identical character counts.2.Algorithm:If len(s) != len(t), return false immediately (edge case).
2.Create a hash map or a frequency array of size 26 (for 'a'-'z').
3.Iterate through (s), incrementing the count for each character.
4.Iterate through (t), decrementing the count for each character.
5.If any count in the frequency table is not zero, return false.
6.Otherwise, return true.
"""

#Hashing method
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS,countT= {},{}
        for i in range(len(s)):
            countS[s[i]]=1 + countS.get(s[i],0)
            countT[t[i]]=1 + countT.get(t[i],0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True

"""
Time complexity is O(n) because the algorithm processes each character of both strings once.

Space complexity is O(n) due to storing character frequencies in hash maps.

"""