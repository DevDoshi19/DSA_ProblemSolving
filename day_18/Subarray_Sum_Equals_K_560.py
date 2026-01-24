# LeetCode Problem 560: Subarray Sum Equals K
# Given an array of integers and an integer k, you need to find the total number of
# continuous subarrays whose sum equals to k.
"""_summary_
Example:
Input: nums = [1,1,1], k = 2
Output: 2


"""


from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_map = {0: 1}
        
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_map:
                count += prefix_map[prefix_sum - k]
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
        
        return count
    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1]
    k = 2
    print(solution.subarraySum(nums, k))  # Output: 2