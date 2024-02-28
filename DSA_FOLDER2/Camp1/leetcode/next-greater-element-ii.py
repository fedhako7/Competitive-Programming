class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        L = len(nums)
        nextG = [-1] * L

        indices = []

        for idx in range(L):
            while indices and nums[idx] > nums[indices[-1]]:
                nextG[indices[-1]] = nums[idx]
                indices.pop()

            indices.append(idx)

        for idx in range(L):
            while nums[idx] > nums[indices[-1]]:
                nextG[indices[-1]] = nums[idx]
                indices.pop()

        return nextG

            