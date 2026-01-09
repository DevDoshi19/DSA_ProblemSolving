from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # solution - 2
        for _ in range(k):
            e = nums.pop()
            nums.insert(0,e)


# Example usage:
nums = [1,2,3,4,5,6,7]
k = 3
Solution().rotate(nums, k)
print(nums)  # Output: [5,6,7,1,2,3,4]

