"""
LeetCode 36. Valid Sudoku
---------------------------------------------------
Key Idea:
Use hash sets to track numbers already seen in:
- Each row
- Each column
- Each 3x3 sub-grid

If a number already exists in any of them,
the Sudoku board is invalid.
---------------------------------------------------
Approach:
1. Create three hash maps:
   - rows    -> stores numbers seen in each row
   - cols    -> stores numbers seen in each column
   - squares -> stores numbers seen in each 3x3 box
2. Traverse every cell in the board.
3. Skip empty cells (".").
4. Check:
   - If number already exists in current row
   - OR current column
   - OR current 3x3 square
   -> return False
5. Otherwise, add the number into all tracking sets.
6. If traversal finishes successfully, return True.
"""

import collections
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)    # Stores values seen in each row
        cols = collections.defaultdict(set)    # Stores values seen in each column
        # Stores values seen in each 3x3 square
        squares = collections.defaultdict(set)    # Key format -> (row_box, col_box)

        # Traverse the entire board
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                square_key = (r // 3, c // 3)  # Identify current 3x3 square

                if (                                    
                    board[r][c] in rows[r]                   
                    or board[r][c] in cols[c]                
                    or board[r][c] in squares[square_key]    
                ):
                    return False
                
                # Add value into tracking sets
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[square_key].add(board[r][c])
        return True

#------------------------------------
# Quick Test
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
sol = Solution()
print(sol.isValidSudoku(board))  # Output: True

"""
Time Complexity:
O(9 × 9) = O(1)  ( Board size is fixed )

Space Complexity:
O(9 × 9) = O(1)  ( Maximum stored elements are constant )
"""