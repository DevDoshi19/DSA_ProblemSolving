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
    
    