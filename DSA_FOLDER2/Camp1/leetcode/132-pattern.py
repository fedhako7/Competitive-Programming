class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        L = len(nums)
        nums.reverse()
        middle = float('-inf')

        indices = deque()

        for idx in range(L):
            if  nums[idx] < middle:
                return True

            while indices and nums[idx] > nums[indices[-1]]:
                middle = nums[indices.pop()]

            indices.append(idx)

        return False