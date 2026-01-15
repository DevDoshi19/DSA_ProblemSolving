"""
Brute Force Approach - Sorting Method

Intuition:
- Sort the array so consecutive numbers become adjacent
- Iterate through sorted array and count consecutive sequences
- Skip duplicates to avoid breaking the sequence

Algorithm:
1. Sort the array
2. Handle empty array edge case
3. Iterate and check if current number is consecutive (num[i] == num[i-1] + 1)
4. If consecutive, increment count; otherwise reset to 1
5. Track the maximum count throughout

Time Complexity: O(n log n) - due to sorting
Space Complexity: O(1) - only using constant extra space

Example: [100, 4, 200, 1, 3, 2]
Sorted: [1, 2, 3, 4, 100, 200]
Result: 4 (sequence [1,2,3,4])
"""

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 0:
            return 0
        count,max_count = 1,1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] :
                continue
            elif nums[i] == nums[i-1]+1 :
                count += 1
            else :
                count = 1 
            max_count = max(count,max_count)

        return max_count
    
# Example 
solution = Solution()
nums=[100,4,200,1,3,2,101,6,7,104,102,103]
print(solution.longestConsecutive(nums=nums))