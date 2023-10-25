class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[p]
                nums[p] = nums[i]
                nums[i] = temp
                p += 1

        return nums
          
