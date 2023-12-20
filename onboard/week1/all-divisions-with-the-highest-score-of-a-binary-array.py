class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        scores = [0] * (len(nums) + 1)
        max_scores = []
        scores.append(0)

        l, r = 1, len(nums) - 1
        while l <= len(nums):
            curr = 1 if nums[l - 1] == 0 else 0
            scores[l] = curr + scores[l - 1]
            l += 1

        while r > -1:
            scores[r] += nums[r]
            r -= 1
            nums[r] += nums[r + 1]

        max_s = max(scores)
        for idx, score in enumerate(scores):
            if score == max_s:
                max_scores.append(idx)

        return max_scores