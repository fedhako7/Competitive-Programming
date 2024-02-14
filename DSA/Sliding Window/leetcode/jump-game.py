class Solution:
    def canJump(self, nums: List[int]) -> bool:
        good = len(nums) - 1

        idx = len(nums) - 2
        steps = 1
        while idx > -1:
            if nums[idx] + idx >= good:
                good = idx

            idx -= 1
            

        return (good == 0)

        