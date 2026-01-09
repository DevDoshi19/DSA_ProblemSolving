from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # solution - 3
        def reverse(nums,left,right):
            while left < right :
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
            
        reverse(nums,n-k,n-1)
        reverse(nums,0,n-k-1)
        reverse(nums,0,n-1)

# Example usage:
nums = [1,2,3,4,5,6,7]
k = 3
Solution().rotate(nums, k)
print(nums)  # Output: [5,6,7,1,2,3,4]

