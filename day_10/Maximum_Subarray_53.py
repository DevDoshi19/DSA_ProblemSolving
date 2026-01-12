from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        count = 0
        
        if len(nums) == 1 :
            return nums[0]
        
        for i in range(0,len(nums)):
            count = count + nums[i]
            max_sum = max(max_sum,count)
            if count < 0 :
                count = 0

        return max_sum 
    
# Example usage:
solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
print(solution.maxSubArray([5,4,-1,7,8]))  # Output: 23
print(solution.maxSubArray([-1]))  # Output: -1
