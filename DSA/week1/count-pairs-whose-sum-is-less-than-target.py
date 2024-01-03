class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        smaller_num = 0
        
        for i in range(len(nums) - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if nums[i] + nums[j] < target:
                    smaller_num += 1


        return smaller_num
