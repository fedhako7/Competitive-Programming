from collections import Counter
class Solution(object):
    def numIdenticalPairs(self, nums):
        nums = Counter(nums)
        goodNum = 0
        for num in nums.keys():
            for frequence in range(nums[num]):
                goodNum += frequence
        return goodNum