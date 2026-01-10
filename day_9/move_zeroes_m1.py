class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0 
        # solution - 1 brute force
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1

        for i in range(k, len(nums)):
            nums[i] = 0       

        # # solution - 2 optimal 
        # if len(nums) == 1:
        #     return 
        
        # i = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0 :
        #         break
        #     i += 1

        # # if i == len(nums):
        # #     return 

        # j = i+1
        # while j < len(nums):
        #     if nums[j] != 0 :
        #         nums[j] ,nums[i] = nums[i],nums[j]
        #         i +=1
                    
        #     j +=1

nums = [0,1,0,3,12]
solution = Solution()
solution.moveZeroes(nums)
