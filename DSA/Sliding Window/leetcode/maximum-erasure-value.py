class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sum_ = 0
        curr_sum = 0
        freq = defaultdict(int)

        left = 0
        for idx in range(len(nums)):
            curr_sum += nums[idx]
            freq[nums[idx]] += 1

            while freq[nums[idx]] > 1:
                freq[nums[left]] -= 1
                curr_sum -= nums[left]
                left += 1

            sum_ = max(sum_, curr_sum)

        
        return sum_