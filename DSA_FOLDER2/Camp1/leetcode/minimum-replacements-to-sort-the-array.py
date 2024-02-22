class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        N = len(nums)
        op = 0
        last = nums[-1]


        for idx in range(N - 2, -1, -1):
            if nums[idx] > last:
                space = ceil(nums[idx] / last)
                last = nums[idx] // space
                op += space - 1

            else:
                last = nums[idx]

        return op