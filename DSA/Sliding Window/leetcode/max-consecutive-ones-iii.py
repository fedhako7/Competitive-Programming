class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        curr_one = 0
        max_one = 0
        rule = 0

        left = 0
        for idx in range(len(nums)):
            curr_one += 1
            if nums[idx] == 0:
                rule += 1

            while rule > k:
                curr_one -= 1
                if nums[left] == 0:
                    rule -= 1

                left += 1

            max_one = max(max_one, curr_one)

        return max_one
        