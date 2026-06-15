"""
Problem: LeetCode 242 - Valid Anagram 

Key Insights:

Edge Case: Different lengths: Always check length first; if len(s) != len(t), they cannot be anagrams.

Detailed Approach: Frequency Counter (Hash Map/Array)
1. Length Check: The function first compares the lengths of \(s\) and \(t\). If they aren't equal, they cannot be anagrams, so it immediately returns False.
2. Frequency Counting: It initializes two dictionaries, countS and countT. It iterates through both strings simultaneously (using their indices), incrementing the character count in each dictionary.
3. Handling Missing Keys: The .get(c, 0) method is used to retrieve the current count of a character. If the character hasn't been seen yet, it defaults to 0 to avoid a KeyError.
4. Comparison Loop: After building the maps, the function iterates through the keys in countS and compares its value (frequency) to the value for the same key in countT.
5. Final Result: If any character count doesn't match, it returns False. If the loop finishes without mismatches, it returns True
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
