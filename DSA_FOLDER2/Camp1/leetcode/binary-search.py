class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def BS(low, high, target):
            if low == high and nums[low] != target:
                return -1

            middle = (low  + high) // 2

            if nums[middle] == target:
                return middle
            if low > high:
                return -1

            elif nums[middle] > target:
                return BS(low, middle - 1, target)

            elif nums[middle] < target:
                return BS(middle + 1, high, target)
                

        
        return BS(0, len(nums) - 1, target)



 