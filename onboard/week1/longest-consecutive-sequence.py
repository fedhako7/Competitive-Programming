class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1 # Count when consecutive nums are appeared, else changes to 1.
        curr = 1 # Count number of of present consecutives
        nums.sort()
        if not nums:
            return 0
        
        for idx in range(1, len(nums)):
            
            if nums[idx] == nums[idx - 1]:
                continue
            if nums[idx] == (nums[idx - 1] + 1):
                curr += 1
                count = max(curr, count)
            else:
                curr = 1
        
        return count   