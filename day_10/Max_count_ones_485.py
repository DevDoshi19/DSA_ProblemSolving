from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0 

        for i in nums:
            if i == 1 :
                count += 1
                max_count = max(max_count,count)
            else:
                count = 0
            
        return max_count
    
# Example usage:
solution = Solution()
print(solution.findMaxConsecutiveOnes([1,1,0,1,1,1]))  # Output: 3