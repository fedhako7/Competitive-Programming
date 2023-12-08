class Solution(object):
    def rearrangeArray(self, nums):
        p = [num for num in nums if num > 0]
        n = [num for num in nums if num < 0]
        l = 0

        for i in range(len(nums)):
            if not i % 2:
                nums[i] = p[l]
            else:
                nums[i] = n[l]
                l += 1
        return nums