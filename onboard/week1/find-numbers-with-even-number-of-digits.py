class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            if not len(str(num)) % 2:
                count += 1

        return count