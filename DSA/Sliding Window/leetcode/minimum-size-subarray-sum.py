class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimal = float('inf')
        sum_ = 0

        left = 0 
        for right in range(len(nums)):
            sum_ += nums[right]

            while sum_ >= target:
                minimal = min(minimal, right - left + 1)
                sum_ -= nums[left]
                left += 1

        
        return minimal if minimal != float('inf') else 0