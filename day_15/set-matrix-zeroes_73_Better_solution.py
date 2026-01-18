"""
Better Approach - Using Extra Space (Row & Column Tracking)

Intuition:
- Instead of marking in the matrix itself, use separate arrays to track
- Use two arrays: one for rows, one for columns
- Mark which rows and columns contain zeros
- Then set zeros in a second pass based on these markers

Algorithm:
1. Create two tracking arrays:
   - rowtrack[i] = -1 means row i should be all zeros
   - coltrack[j] = -1 means column j should be all zeros

2. First Pass - Identify zeros:
   - Scan entire matrix
   - When we find matrix[i][j] == 0:
     * Mark rowtrack[i] = -1
     * Mark coltrack[j] = -1

3. Second Pass - Set zeros:
   - Scan entire matrix again
   - If rowtrack[i] == -1 OR coltrack[j] == -1:
     * Set matrix[i][j] = 0

Example Walkthrough:
Input: [[1,1,1],
        [1,0,1],
        [1,1,1]]

Step 1: Initialize tracking arrays
rowtrack = [0, 0, 0]
coltrack = [0, 0, 0]

Step 2: Find zero at (1,1)
rowtrack = [0, -1, 0]  ← row 1 marked
coltrack = [0, -1, 0]  ← col 1 marked

Step 3: Set zeros based on markers
- (0,1): coltrack[1] == -1 → set to 0
- (1,0): rowtrack[1] == -1 → set to 0
- (1,1): already 0
- (1,2): rowtrack[1] == -1 → set to 0
- (2,1): coltrack[1] == -1 → set to 0

Output: [[1, 0, 1],
         [0, 0, 0],
         [1, 0, 1]]

Time Complexity: O(m * n)
- First pass: O(m * n) - scan entire matrix once
- Second pass: O(m * n) - scan entire matrix once
- Total: O(m * n) + O(m * n) = O(m * n)
- Much better than previous O(m * n * (m + n)) approach!

Space Complexity: O(m + n)
- rowtrack array: O(m) space for m rows
- coltrack array: O(n) space for n columns
- Total extra space: O(m + n)
- Trade-off: Using extra space for better time complexity

Comparison with Previous Approach:
Previous (Infinity Marking):
- Time: O(m * n * (m + n)) ✗ Slower
- Space: O(1) ✓ No extra space

Current (Row/Col Tracking):
- Time: O(m * n) ✓ Optimal time
- Space: O(m + n) ✗ Extra space used

Pros:
✓ Optimal time complexity O(m * n)
✓ Clean and easy to understand
✓ Only two passes through matrix
✓ No risk of conflicts with existing values
✓ Standard interview solution

Cons:
✗ Uses extra O(m + n) space
✗ Not truly "in-place" due to extra arrays

Next Level Optimization:
- Can achieve O(1) space by using first row/column as markers
- More complex but truly constant space

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
        row = len(matrix)
        col = len(matrix[0])
        
        # Create tracking arrays to mark which rows/cols need zeros
        rowtrack = [0 for _ in range(row)]  # Track rows with zeros
        coltrack = [0 for _ in range(col)]  # Track columns with zeros
        
        # First pass: Identify which rows and columns contain zeros
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rowtrack[i] = -1  # Mark this row
                    coltrack[j] = -1  # Mark this column
        
        # Second pass: Set zeros based on markers
        for i in range(row):
            for j in range(col):
                if rowtrack[i] == -1 or coltrack[j] == -1:
                    matrix[i][j] = 0

# Example
solution = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
solution.setZeroes(matrix)
print(matrix)  # Output: [[1,0,1],[0,0,0],[1,0,1]]