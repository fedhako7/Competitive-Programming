class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        l, r = 0, len(nums) - 1
        count = 0
        while l < r and l < len(nums) - 1 and r > -1:
            if nums[l] + nums[r] == k:
                count += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1

        return count
