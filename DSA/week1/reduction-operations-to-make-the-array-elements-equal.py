class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        nums = list(set(nums))
        nums.sort()
        
        tot_op = 0 
        for idx in range(len(nums) -1, 0, -1):
            tot_op += (freq[nums[idx]])
            freq[nums[idx - 1]] += freq[nums[idx]]


        return tot_op

