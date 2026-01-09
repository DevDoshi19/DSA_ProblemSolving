from typing import List
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [nums[nums[i]] for i in range(len(nums))]

        return ans    
    
# Example usage:
nums = [0,2,1,5,3,4]
solution = Solution().buildArray(nums)
print(solution)  # Output: [0, 1, 2, 4,
