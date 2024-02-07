class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]

        for idx in range(1, len(nums)):
            if nums[idx - 1] > 0:
                nums[idx] += nums[idx - 1]

            max_sum = max(nums[idx], max_sum)


        return max_sum

            