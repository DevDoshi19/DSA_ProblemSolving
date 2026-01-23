from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        # Step 1: Calculate prefix products (left to right)
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        # Step 2: Calculate suffix products (right to left) and multiply
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result
    
# Example usage:
solution = Solution()
nums = [1, 2, 3, 4]
print(solution.productExceptSelf(nums))  # Output: [24, 12, 8, 6]
