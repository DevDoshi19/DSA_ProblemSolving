from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1  # Search left
            else:
                left = mid + 1   # Search right
        
        return -1
    
# Example usage:
sol = Solution()
print(sol.search([-1,0,3,5,9,12], 9))  # Output: 4
print(sol.search([-1,0,3,5,9,12], 2))  # Output: -1