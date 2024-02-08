class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0]

        left_p = [0] * len(nums)
        right_p = [0] * len(nums)

        for idx in range(1, len(nums)):
            left_p[idx] = nums[idx - 1] + left_p[idx - 1]

        for idx in range(len(nums) - 2, -1, -1):
            right_p[idx] = nums[idx + 1] + right_p[idx + 1]

        print(left_p)
        print(right_p)

        for idx in range(len(nums)):
            left_p[idx] = abs(right_p[idx] - left_p[idx])

        return left_p