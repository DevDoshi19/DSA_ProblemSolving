"""remove negative numbers from the 
list in-place and return the new length of the list"""
nums = [3, -1, 0, -5, 8, -2]

k = 0 
for i in range(len(nums)):
    if nums[i] >= 0 :
        nums[k] = nums[i]
        k +=1

print(nums[0:k])
print(k)