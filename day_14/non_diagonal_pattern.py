# Print the non-diagonal pattern from the given 2D array
# Example Input:

nums = [[5,10,8],[7,6,3],[2,1,9]]

row = len(nums)
col = len(nums[0])

for i in range(row):
    for j in range(col):
        if j == row - i - 1:
            print(nums[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()

'''
what we have done here is we have iterated through each element of the 2D array
and printed the element only if it is not on the diagonal (i.e., when column index j is not equal to row index i)

- otherwise we print a space to maintain the structure of the array

- The time complexity of this approach is O(n^2) where n is the number of rows (or columns) in the 2D array
- The space complexity is O(1) as we are not using any extra space that grows

with the input size.
~ Example Output:
  
        8
     6    
  2

'''