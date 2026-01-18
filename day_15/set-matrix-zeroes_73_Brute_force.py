from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def mark_infi(matrix,row,col):

            r = len(matrix)
            c = len(matrix[0])

            for i in range(0,r):
                if matrix[i][col] != 0 :
                    matrix[i][col] = float("inf")

            for j in range(0,c):
                if matrix[row][j] != 0 :
                    matrix[row][j] = float("inf")

        row = len(matrix)
        col = len(matrix[0])
        for i in range(0,row):
            for j in range(0,col):
                if  matrix[i][j] == 0 :
                   mark_infi(matrix,i,j)
                
        for i in range(0,row):
            for j in range(0,col):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0 

# Example
solution = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
solution.setZeroes(matrix=matrix)
print(matrix)  # Output: [[1,0,1],[0,0,0],[1,0,1]]