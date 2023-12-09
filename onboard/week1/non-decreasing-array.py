class Solution(object):
    def checkPossibility(self, nums):
        if len(nums) <= 2:
            return True
        # Find the first number where the nums is jumbled
        idx = ''
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                idx = i
                break

            # return True if nums is already sorted
            if i == len(nums) - 1:
                return True

        # Pop the the element where nums jumbled, 
        # compare nums with sorted nums to check wheather nums is jumbled only once or not
        # Do  the same for idx-1 if not equal still return False
        poped = nums.pop(idx)
        flag = False

        if sorted(nums) == nums:
            flag = True
            
        else:
            nums.insert(idx, poped)
            del nums[idx - 1]
            if sorted(nums) == nums:
                flag = True
        return flag