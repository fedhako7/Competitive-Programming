class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        print(nums)
        write, read = 0, 0
        while read < len(nums):
            while read < len(nums) and nums[read] == 0:
                read += 1

            if read < len(nums):
                print()
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
                read += 1

        return nums
