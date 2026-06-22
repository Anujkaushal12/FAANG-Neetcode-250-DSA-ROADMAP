"""
LeetCode 304 — Range Sum Query 2D - Immutable
Key Idea

Use a 2D Prefix Sum Matrix to preprocess the matrix.

Instead of calculating the sum of a submatrix every time (which would take O(rows × cols)), we precompute cumulative sums so that each query can be answered in O(1) time.

Core Concept

sumMat[r][c] stores the sum of all elements from:

(0,0) → (r-1,c-1)

A padded row and column of zeros are added to simplify calculations and avoid boundary checks.

Approach:-
        Step 1: Build Prefix Sum Matrix

        For every cell:
                Current Prefix Sum = Row Prefix + Sum Above

        Formula:
                sumMat[r+1][c+1] = rowPrefix + sumMat[r][c+1]

                Where:
                    rowPrefix = sum of current row up to column c
                    sumMat[r][c+1] = cumulative sum from rows above
        
        Step 2: Answer Queries
            
        To find the sum of a rectangle:
                                        (row1,col1) → (row2,col2)

        Use Inclusion-Exclusion Principle:
                                        Region Sum  = BottomRight - Above - Left  + TopLeft

        Formula:
            sum =sumMat[r2][c2]
                - sumMat[r1-1][c2]
                - sumMat[r2][c1-1]
                + sumMat[r1-1][c1-1]

"""

from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])

        # Prefix sum matrix with extra row and column
        self.sumMat = [[0] * (cols + 1) for _ in range(rows + 1)]

        # Build prefix sum matrix
        for r in range(rows):

            row_prefix = 0

            for c in range(cols):

                # Running sum for current row
                row_prefix += matrix[r][c]

                # Sum from rows above
                above = self.sumMat[r][c + 1]

                # Store cumulative sum
                self.sumMat[r + 1][c + 1] = row_prefix + above

    def sumRegion(self,row1: int,col1: int,row2: int,col2: int) -> int:
        # Shift by 1 because of extra padding row/column
        r1, c1 = row1 + 1, col1 + 1
        r2, c2 = row2 + 1, col2 + 1

        # Inclusion-Exclusion Principle
        bottom_right = self.sumMat[r2][c2]
        above = self.sumMat[r1 - 1][c2]
        left = self.sumMat[r2][c1 - 1]
        top_left = self.sumMat[r1 - 1][c1 - 1]

        return bottom_right - above - left + top_left
    
"""
Complexity Analysis

Constructor:-
Building prefix matrix: 
                        O(rows × cols)

Query:-
Each query uses only four lookups:
                                O(1)

Space Complexity

Prefix matrix size: 
                (rows + 1) × (cols + 1)

Therefore:
        O(rows × cols)

"""