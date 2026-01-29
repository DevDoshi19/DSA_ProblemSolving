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