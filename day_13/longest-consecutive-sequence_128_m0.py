"""
Brute Force Approach - Nested Loop Method

Intuition:
- For each number, try to build a consecutive sequence starting from it
- Use inner while loop to check if next consecutive numbers exist in array
- Track the maximum sequence length found

Algorithm:
1. Iterate through each number in the array (outer loop)
2. For each number, use while loop to check if num+1, num+2, num+3... exist
3. Count how many consecutive numbers we can find
4. Update max_count with the longest sequence
5. Reset count for next iteration

Time Complexity: O(n^2) 
- Outer loop: O(n) - iterate through all numbers
- Inner while loop: O(n) - 'in' operator on list is O(n)
- Worst case: checking n elements for each of n numbers

Space Complexity: O(1) - only using constant extra space

Example: [100, 4, 200, 1, 3, 2]
- Start at 100: finds 100 only (length = 1)
- Start at 4: finds 4 only (length = 1)  
- Start at 1: finds 1→2→3→4 (length = 4) ✓
- Result: 4

⚠️ Issue: Very inefficient due to repeated lookups
Can be optimized to O(n) using HashSet!
"""

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        max_count = 0
        count = 1
        for i in range(n):
            num = nums[i]
            while num + 1 in nums:
                count += 1
                num += 1
            max_count = max(max_count, count)
            count = 1
        return max_count
    
# Example 
solution = Solution()
nums=[100,4,200,1,3,2,101,6,7,104,102,103]
print(solution.longestConsecutive(nums=nums))