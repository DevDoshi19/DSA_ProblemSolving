"""
Spiral Matrix Traversal - Layer-by-Layer Approach

Intuition:
- Traverse the matrix in a spiral pattern: right → down → left → up
- Process the matrix layer by layer, from outer to inner
- Use four boundaries (top, bottom, left, right) to track current layer
- After completing each direction, shrink the corresponding boundary

Algorithm:
1. Initialize four boundaries:
   - top = 0 (topmost row)
   - bottom = len(matrix) - 1 (bottommost row)
   - left = 0 (leftmost column)
   - right = len(matrix[0]) - 1 (rightmost column)

2. While boundaries don't cross (left <= right AND top <= bottom):
   
   a) Traverse RIGHT: Move along top row from left to right
      - Add matrix[top][left...right] to result
      - Increment top (this row is done)
   
   b) Traverse DOWN: Move along right column from top to bottom
      - Add matrix[top...bottom][right] to result
      - Decrement right (this column is done)
   
   c) Traverse LEFT: Move along bottom row from right to left
      - Check if top <= bottom (avoid duplicate rows)
      - Add matrix[bottom][right...left] to result
      - Decrement bottom (this row is done)
   
   d) Traverse UP: Move along left column from bottom to top
      - Check if left <= right (avoid duplicate columns)
      - Add matrix[bottom...top][left] to result
      - Increment left (this column is done)

3. Return result array

Visual Example:
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

Layer 1 (outer):
→ → →
1  2  3
↓     ↓
4  5  6
↓     ↓
7  8  9
← ← ←

Step-by-step:
1. Right: [1,2,3]           top=0, left=0→2
2. Down:  [1,2,3,6,9]       right=2, top=1→2
3. Left:  [1,2,3,6,9,8,7]   bottom=2, right=1→0
4. Up:    [1,2,3,6,9,8,7,4] left=0, bottom=1→1
5. Center: [1,2,3,6,9,8,7,4,5]

Result: [1,2,3,6,9,8,7,4,5]

Edge Cases Handled:
1. Empty matrix: if not matrix or not matrix[0] → return []
2. Single row: Only right traversal happens
3. Single column: Only down traversal happens
4. Single element: All traversals happen but only one element

Why we need if statements before left and up traversal:
- After moving top down and right left, boundaries might cross
- Example: Single row [[1,2,3]]
  * After right: top=1, bottom=0 → top > bottom
  * Skip left/up traversal to avoid re-processing
- Prevents duplicate elements in result

Boundary Movement Pattern:
Direction  | Boundary Changed | How
-----------|------------------|-----
Right  →   | top++            | Move down after traversing top row
Down   ↓   | right--          | Move left after traversing right column
Left   ←   | bottom--         | Move up after traversing bottom row
Up     ↑   | left++           | Move right after traversing left column

Time Complexity: O(m * n)
- Visit each element exactly once
- m = number of rows, n = number of columns
- Total elements = m * n

Space Complexity: O(1)
- Only using result array (which is required for output)
- Boundary variables (top, bottom, left, right) use O(1) space
- Not counting output space, auxiliary space is O(1)

Key Insights:
1. Four boundaries control the spiral traversal
2. Shrink boundaries after each direction
3. Conditional checks prevent boundary crossing
4. Pattern repeats until all elements visited

Common Mistakes to Avoid:
❌ Forgetting to check boundaries before left/up traversal
❌ Using wrong loop ranges (off-by-one errors)
❌ Not handling edge cases (empty, single row/column)
❌ Moving boundaries at wrong time

Interview Tips:
- Draw the matrix and trace through manually
- Explain boundary shrinking clearly
- Mention edge case handling
- Practice with different matrix sizes
"""

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Handle edge case: empty matrix
        if not matrix or not matrix[0]:
            return []
        
        # Initialize four boundaries
        top, left = 0, 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1
        result = []
        
        # Continue while boundaries don't cross
        while left <= right and top <= bottom:
            
            # 1. Traverse RIGHT: along top row from left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  # Move top boundary down
            
            # 2. Traverse DOWN: along right column from top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # Move right boundary left
            
            # 3. Traverse LEFT: along bottom row from right to left
            if top <= bottom:  # Check if bottom row still exists
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  # Move bottom boundary up
            
            # 4. Traverse UP: along left column from bottom to top
            if left <= right:  # Check if left column still exists
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # Move left boundary right
        
        return result
    
solution = Solution()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(solution.spiralOrder(matrix))  # Output: [1,2,3,6,9,8,7,4,5]
