class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)

        alice, bob = 0, 1
        while bob < len(nums):
            arr[alice], arr[bob] = arr[bob], arr[alice]
            alice += 2
            bob += 2

        return arr
