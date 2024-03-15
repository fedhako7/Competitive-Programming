class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()

        low = -1
        high = len(nums) - 1
        while low + 1 < high:
            mid = (low + high) // 2

            if nums[mid] < nums[-1]:
                low = mid
            else:
                high = mid


        greaterIndex = low
        if greaterIndex == -1:
            return 0
            

        low = 0
        high = len(nums)
        while low + 1 < high:
            mid = (low + high) // 2

            if nums[mid] > nums[0]:
                high = mid
            else:
                low = mid


        smallerIndex = high
        if smallerIndex == len(nums):
            return 0


        return (greaterIndex - smallerIndex) + 1