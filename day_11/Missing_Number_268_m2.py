from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {
            i: 0 for i in range(n + 1)
        }
        
        for i in nums :
            freq[i] += 1

        for key, value in freq.items():
            if value == 0 :
                return key

# Example usage:
solution = Solution()
print(solution.missingNumber([3,0,1]))  # Output: 2
print(solution.missingNumber([0,1,2,3,4,5,6,7]))    # Output: 8
