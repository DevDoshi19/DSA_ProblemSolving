from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        n = len(nums)
        
        # Find lower bound (first occurrence)
        left, right = 0, n - 1
        lb = n
        
        while left <= right :
            mid = (left+right)//2
            if nums[mid] >= target:
                lb = mid
                right = mid - 1 
            else :
                left = mid+1
        
        left,right = 0,n-1
        ub = n 
        while left <= right :
            mid = (left+right)//2
            if nums[mid] > target:
                ub = mid
                right = mid - 1 
            else :
                left = mid+1

        if lb < n and ub > 0 and lb <= ub-1 : 
            return [lb,ub-1]

        return [-1,-1]       
    
# Example usage:
sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8))  # Output: [3, 4]
print(sol.searchRange([5,7,7,8,8,10], 6))  # Output: [-1, -1]
# LeetCode Problem 34: Find First and Last Position of Element in Sorted Array - Medium
# Given an array of integers nums sorted in ascending order, find the starting and ending position of
# a given target value. If the target is not found in the array, return [-1, -1].