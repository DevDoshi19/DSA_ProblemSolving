# Brute Force Approach

nums = [3,1,-2,-5,2,-4]
n = len(nums)

pos=[]
neg=[]

for num in nums :
    if num > 0:
        pos.append(num)
    else:
        neg.append(num)
        
for i in range(0,len(pos)):
    nums[i*2] = pos[i]
    nums[(i*2)+1] = neg[i]
    
print(nums)