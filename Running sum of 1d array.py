class Solution(object):
    def runningSum(self, nums):
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            nums[i] = sum

        return nums
