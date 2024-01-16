class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = []
        prefix.append(nums[0])

        for idx in range(1, len(nums)):
            val = nums[idx] + prefix[idx - 1]
            prefix.append(val)

        if len(nums) == 1 or prefix[-1] - prefix[0] == 0:
            return 0

        for idx in range(1, len(nums)):
            if prefix[idx - 1] == prefix[-1] - prefix[idx]:
                return idx

        return -1

        