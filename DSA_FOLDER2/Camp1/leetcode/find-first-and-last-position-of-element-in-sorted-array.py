class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #Binary Search

        low = -1
        start = len(nums)
        while low + 1 < start:
            mid = (low + start) // 2
            if nums[mid] < target:
                low = mid
            else:
                start = mid


        if start == len(nums) or nums[start] > target:
            return [-1, -1]


        end = -1
        high = len(nums)
        while end + 1 < high:
            mid = (end + high) // 2
            if nums[mid] > target:
                high = mid
            else:
                end = mid


        return [start, end]





















        #Two pointer
        '''if len(nums) == 0:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] != target:
                 left += 1
                 
            if nums[right] != target:
                 right -= 1

            if left < len(nums) and right > -1 and nums[left] == nums[right] == target:
                return [left, right]

        return [-1, -1]'''


        


        








