from typing import List
class Solution:
    def twoSum(self, nums : List[int], target)-> List[int]:
        hash_map = {}
        n = len(nums)

        for i in range(n):
            reamining = target - nums[i]
            if reamining in hash_map:    
                return [hash_map[reamining], i]
            hash_map[nums[i]] = i

        return []

nums = [5,9,1,2,3,35,16,17,15]
target = 16

solution = Solution()
print(solution.twoSum(nums, target))  # Output: [0, 6]
