class Solution:
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        l, r = 0, 0
        ans = nums[0]
        cnt = len(nums)
        isvalid = False
        while l < len(nums) and r < len(nums):
            if ans < s:
                if r == len(nums) - 1:
                    break
                r += 1
                ans += nums[r]
            else:
                isvalid = True
                cnt = min(cnt, r - l + 1)
                ans -= nums[l]
                l += 1
            
            
        return cnt if isvalid else 0
