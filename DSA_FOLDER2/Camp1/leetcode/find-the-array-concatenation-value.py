class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        turnL = True
        value = 0

        while l <= r:
            if l == r:
                value += int(str(nums[l]))
                l += 1

            else:
                value += (int(str(nums[l]) + str(nums[r])))
                l += 1
                r -= 1

        return value

