from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = (n*(n+1))//2
        actual_sum = 0
        for i in nums :
            actual_sum += i
        return expected - actual_sum    
    
# Example usage:
solution = Solution()
print(solution.missingNumber([3,0,1]))  # Output: 2
print(solution.missingNumber([0,1]))    # Output: 2
