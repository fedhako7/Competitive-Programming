class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = -1
        high = len(nums) - 1

        while low + 1 < high:
            mid = (low + high) // 2

            if nums[mid] < nums[high]:
                high = mid

            else:
                low = mid

        return nums[high]