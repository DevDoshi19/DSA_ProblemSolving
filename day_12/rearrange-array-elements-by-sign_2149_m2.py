from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = [0] * n
        posIndex = 0
        negIndex = 1
        
        for num in nums:
            if num > 0:
                result[posIndex] = num
                posIndex += 2
            else:
                result[negIndex] = num
                negIndex += 2
        
        return result
    
# Example usage:
solution = Solution()
print(solution.rearrangeArray([3,1,-2,-5,2,-4]))
# Output: [3,-2,1,-5,2,-4]