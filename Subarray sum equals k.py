class Solution(object):
    def subarraySum(self, nums, k):
        res = 0
        curr_sum = 0 
        prefix_sum = {0 : 1}
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            res += prefix_sum.get(diff, 0)
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
        return res
