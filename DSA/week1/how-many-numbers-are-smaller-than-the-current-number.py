class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        smaller = {}
        nums2 = sorted(nums)

        for i, a in enumerate(nums2):
            if a not in smaller:
                smaller[a] = i

        for i in range(len(nums)):
            nums[i] = smaller[nums[i]]

        return nums
        