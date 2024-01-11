class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, 0

        while right < len(nums):
            while right < len(nums) and nums[right] == val:
                right += 1

            if left < len(nums) and right < len(nums):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1


        return left

        