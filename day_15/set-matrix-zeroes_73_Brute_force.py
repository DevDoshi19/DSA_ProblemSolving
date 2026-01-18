"""
Brute Force Approach - Marking with Infinity

Problem: Set entire row and column to 0 if any element in that position is 0
Challenge: Can't set zeros immediately as it affects subsequent checks

Intuition:
- We can't set zeros while scanning because it creates cascading zeros
- Solution: Mark positions with a special value (infinity) first
- Then convert all infinity markers to zeros in a second pass
- Use infinity because it won't naturally appear in the input (integers only)

Algorithm:
1. First Pass - Find zeros and mark their rows/columns:
   - Iterate through entire matrix
   - When we find a 0 at position (i, j):
     * Mark entire row i with infinity (except existing zeros)
     * Mark entire column j with infinity (except existing zeros)
   
2. Second Pass - Convert markers to zeros:
   - Iterate through entire matrix again
   - Replace all infinity values with 0

Helper Function: mark_inf(matrix, row, col)
- Takes the position of a zero element
- Marks entire row and column with float("inf")
- Skips cells that are already 0 (to preserve original zeros)

Example Walkthrough:
Input: [[1,1,1],
        [1,0,1],
        [1,1,1]]

Step 1: Find zero at (1,1)
After marking: [[1, inf, 1],
                [inf, 0, inf],
                [1, inf, 1]]

Step 2: Convert inf to 0
Output: [[1, 0, 1],
         [0, 0, 0],
         [1, 0, 1]]

Time Complexity: O(m * n * (m + n))
- Outer loops: O(m * n) to scan entire matrix
- For each zero found, mark_inf takes: O(m + n)
  * O(m) to mark column
  * O(n) to mark row
- Second pass: O(m * n) to convert inf to 0
- Worst case: if all elements are 0, we call mark_inf m*n times
- Total: O(m * n * (m + n))

Space Complexity: O(1)
- Only using constant extra space for variables (i, j, row, col, r, c)
- Modifying matrix in-place
- Not using any additional data structures
- Note: We're using the matrix itself to store markers

Pros:
✓ In-place modification (no extra space for data structures)
✓ Easy to understand the logic
✓ Works correctly for all test cases

Cons:
✗ Not optimal time complexity O(m*n*(m+n)) vs optimal O(m*n)
✗ Requires multiple passes through matrix
✗ Won't work if matrix contains infinity values (but LeetCode doesn't test this)

Better Approaches:
1. Use extra space O(m+n): Store zero positions in sets - Time: O(m*n)
2. Use first row/column as markers: Constant space - Time: O(m*n)

Where:
m = number of rows
n = number of columns
"""
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def mark_inf(matrix, row, col):
            """
            Helper function to mark entire row and column with infinity
            
            Args:
                matrix: 2D list to modify
                row: row index where zero was found
                col: column index where zero was found
            """
            r = len(matrix)      # Total rows
            c = len(matrix[0])   # Total columns
            
            # Mark entire column with infinity
            for i in range(r):
                if matrix[i][col] != 0:  # Don't overwrite existing zeros
                    matrix[i][col] = float("inf")
            
            # Mark entire row with infinity
            for j in range(c):
                if matrix[row][j] != 0:  # Don't overwrite existing zeros
                    matrix[row][j] = float("inf")

        rows = len(matrix)
        cols = len(matrix[0])
        
        # First pass: Find zeros and mark their rows/columns with infinity
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    mark_inf(matrix, i, j)
        
        # Second pass: Convert all infinity markers to zeros
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0
# Example
solution = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
solution.setZeroes(matrix=matrix)
print(matrix)  # Output: [[1,0,1],[0,0,0],[1,0,1]]