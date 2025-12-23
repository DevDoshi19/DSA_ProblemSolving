# Function to check if there exists a pair with given sum in a sorted array
def validate(nums,left,right,target):
    while left<right:
        s = nums[left] + nums[right]
        if s == target:
            return True
        elif s < target:
            left += 1
        else:
            right -= 1
    return False 

nums=[1,2,3,4,6,8,9]
target = 10
left,right= 0 ,len(nums)-1

print(validate(nums,left,right,target))