class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        minMax = nums[0]
        idx = 0
        tot = 0
        while idx < len(nums):
            tot += nums[idx]
            minMax = max(ceil(tot / (idx + 1)), minMax)
            idx += 1
        
        return (minMax)