"""
Optimal Approach - HashSet Method

Intuition:
- Use a HashSet for O(1) lookup time
- Only start counting from the beginning of a sequence (num-1 not in set)
- This ensures each number is processed at most twice

Algorithm:
1. Convert array to HashSet for O(1) lookups
2. Iterate through each number in the set
3. Check if current number is the START of a sequence (num-1 not in set)
4. If yes, count consecutive numbers (num+1, num+2, ...) using while loop
5. Track the maximum sequence length found

Time Complexity: O(n)
- Creating set: O(n)
- Iterating through set: O(n)
- Each number visited at most twice (once as start, once in while loop)
- HashSet lookup: O(1)

Space Complexity: O(n) - for storing elements in HashSet

Example: [100, 4, 200, 1, 3, 2]
HashSet: {1, 2, 3, 4, 100, 200}
- 100: (99 not in set) → start counting → 100 only (length=1)
- 4: (3 in set) → skip (not a start)
- 200: (199 not in set) → start counting → 200 only (length=1)
- 1: (0 not in set) → start counting → 1→2→3→4 (length=4) ✓
- Result: 4

Key Insight: By only counting from sequence starts, we avoid redundant work!
"""

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        max_count = 0

        for num in num_set:
            if num -1 not in num_set:
                x = num
                count = 1
                while x+1 in num_set:
                    x+=1
                    count += 1
                max_count = max(max_count, count)
        return max_count
        
# Example 
solution = Solution()
nums=[100,4,200,1,3,2,101,6,7,104,102,103]
print(solution.longestConsecutive(nums=nums))