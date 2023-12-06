class Solution(object):
    def decompressRLElist(self, nums):
        decomps = []

        for idx in range(len(nums) - 1):
            if idx % 2 == 1:
                continue
            else:
                val = [nums[idx + 1]] * nums[idx]
                decomps.extend(val)
        
        return decomps