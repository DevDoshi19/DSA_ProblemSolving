from typing import List
def getConcatenation(self, nums: List[int]) -> List[int]:
        nums = nums + nums
        return nums

# Example usage:
nums = [1, 2, 3]
solution = getConcatenation(None, nums)
print(solution)  # Output: [1, 2, 3, 1, 2, 3]

