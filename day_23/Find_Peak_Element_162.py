from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # Compare mid with its right neighbor
            if nums[mid] > nums[mid + 1]:
                # Peak is on the left side (or mid itself)
                right = mid
            else:
                # Peak is on the right side
                left = mid + 1
        
        return left
    
# Example usage:
sol = Solution()
print(sol.findPeakElement([1,2,3,1]))  # Output: 2
print(sol.findPeakElement([1,2,1,3,5,6,4]))  # Output: 5
# LeetCode Problem 162: Find Peak Element - Medium