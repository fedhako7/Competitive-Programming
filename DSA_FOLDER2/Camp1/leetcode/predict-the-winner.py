class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        

        def canWin(nums, left, right):
            if left == right:
                return nums[left]

            preferL = nums[left] - canWin(nums, left + 1, right)
            preferR = nums[right] - canWin(nums, left, right - 1)

            return max(preferL, preferR)


        return canWin(nums, 0, len(nums) - 1) >= 0