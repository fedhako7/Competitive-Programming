class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_num = 0 if len(nums) == 1 or nums[0] > nums[1] else len(nums) - 1

        for idx in range(1, len(nums) - 1):
            if nums[idx - 1] < nums[idx] and nums[idx] > nums[idx + 1]:
                return idx

        return max_num