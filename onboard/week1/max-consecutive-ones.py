class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        l, consec_one = 0, 0

        for r, n in enumerate(nums):
            if nums[r] == 0:
                l =  r + 1
            consec_one = max(consec_one, r - l + 1)

        return consec_one
