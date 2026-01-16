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