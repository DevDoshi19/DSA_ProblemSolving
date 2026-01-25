from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lb = n 
        low,high = 0,n-1
        while low <= high :
            mid = (low+high)//2
            if nums[mid] >= target :
                high = mid-1
                lb = mid

            else :
                low = mid+1

        return lb 
    
solution = Solution()
print(solution.searchInsert([1,3,5,6],5))  # Output: 2
print(solution.searchInsert([1,3,5,6],2))  # Output: 1
print(solution.searchInsert([1,3,5,6],7))  # Output: 4