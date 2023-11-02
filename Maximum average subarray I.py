
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        current = 0
        for i in range(k):
            current += nums[i]
            max_sum = current
        for i in range(k, len(nums)):
            current += (nums[i] - nums[i - k])
            max_sum = max(max_sum, current)

        return max_sum/float(k)
