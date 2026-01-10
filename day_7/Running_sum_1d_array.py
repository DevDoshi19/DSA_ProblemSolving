from typing import List
def runningSum(self, nums: List[int]) -> List[int]:
    for i in range(1,len(nums)):
        nums[i] += nums[i-1] 
    return nums    

# Example usage:
nums = [1,2,3,4]
solution = runningSum(None, nums)
print(solution)  # Output: [1, 3, 6, 10]
