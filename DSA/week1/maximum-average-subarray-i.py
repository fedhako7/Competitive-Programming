class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_ = sum(nums[ :k])
        max_ = sum(nums[ :k])
     
        for i in range(k, len(nums)):
            sum_ += (nums[i] - nums[i - k])
            max_ = max(max_, sum_)

        
        return (max_ / k)


        