class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_array = 0
        prefix_sums = {0 : 1}
        curr = 0

        for num in nums:
            curr += num
            diff = curr - k

            sub_array += prefix_sums.get(diff, 0)
            prefix_sums[curr] = prefix_sums.get(curr, 0) + 1

        return sub_array