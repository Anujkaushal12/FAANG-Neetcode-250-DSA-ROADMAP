"""
Problem: LeetCode 271 - Encode and Decode Strings
------------------------------------------------------
key Idea:
Store each string in this format:- 
                                 length#string
------------------------------------------------------
Detailed Approach:-

//Encode
1.Traverse each string in the list.
2.Append:
        ->length of string
        ->#
        ->actual string
3.Return the final encoded string.

//Decode
1.Traverse the encoded string.
2.Read characters until # to get the length.
3.Convert length into integer.
4.Extract the next length characters.
5.Add extracted string to result list.
6.Continue until entire string is processed.
"""
from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j=i
            while s[j] != "#":
                j +=1
            length=str[i:j]
            res.append(str[j+1:j+1+length])
            i=j+1+length
        return res
"""
Encode:-
Time Complexity: O(n)

Decode:-
Time Complexity: O(n)

Encode:-
Space Complexity: O(n) for storing encoded string.

Decode:-
Space Complexity: O(n) for storing decoded output list.
"""