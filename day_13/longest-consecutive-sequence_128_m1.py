from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 0:
            return 0
        count,max_count = 1,1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] :
                continue
            elif nums[i] == nums[i-1]+1 :
                count += 1
            else :
                count = 1 
            max_count = max(count,max_count)

        return max_count
    
# Example 
solution = Solution()
nums=[100,4,200,1,3,2,101,6,7,104,102,103]
print(solution.longestConsecutive(nums=nums))