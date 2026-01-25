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