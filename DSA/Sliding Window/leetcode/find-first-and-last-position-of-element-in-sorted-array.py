class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] != target:
                 left += 1
                 
            if nums[right] != target:
                 right -= 1

            if left < len(nums) and right > -1 and nums[left] == nums[right] == target:
                return [left, right]

        return [-1, -1]

        