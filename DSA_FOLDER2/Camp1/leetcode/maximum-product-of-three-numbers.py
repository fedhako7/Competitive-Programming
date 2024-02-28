class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        choice1 = nums[0] * nums[1] * nums[-1]
        choice2 = nums[-1] * nums[-2] * nums[-3]
        return max(choice1, choice2)


        
        