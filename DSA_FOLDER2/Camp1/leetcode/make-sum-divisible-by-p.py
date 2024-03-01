class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tot = sum(nums)
        target = tot % p

        if target == 0:
            return 0

        mods = defaultdict(int)
        prefix = 0
        minSub = float('inf')
        for idx, num in enumerate(nums):
            print(idx, num)
            prefix += num
            prefix %= p
            if prefix == target:
                minSub = min(minSub, idx + 1)

            if (prefix - target) % p in mods:
                minSub = min(minSub, idx - mods[(prefix - target) % p])

            mods[prefix] = idx
        
        return minSub if (minSub != len(nums) and minSub != float('inf')) else -1 
                