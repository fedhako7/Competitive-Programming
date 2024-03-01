class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        L = len(nums)

        for idx in range(L):
            if nums[idx] % 2:
                nums[idx] = 1

            else: 
                nums[idx] = 0

        freq = defaultdict(int)
        freq[0] = 1
        prefix = 0
        niceArr = 0
        for num in nums:
            prefix += num
            niceArr += freq[prefix - k]
            freq[prefix] += 1

        return niceArr        