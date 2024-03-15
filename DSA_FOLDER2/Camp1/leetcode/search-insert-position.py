class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        high = len(nums)
        low = -1

        while low + 1 < high:
            idx = (low + high) // 2

            if nums[idx] < target:
                low = idx

            elif nums[idx] == target:
                return idx
            
            else:
                high = idx

        return high 
        