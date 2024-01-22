class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sub_arr = 0 
        seen = {0:1}
        sum_ = 0
       
        for num in nums:
            sum_ += num

            if sum_ - goal in seen:
                sub_arr += seen[sum_ - goal]

            seen[sum_] = seen.get(sum_, 0) + 1

        return sub_arr