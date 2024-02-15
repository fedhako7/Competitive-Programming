class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 1:
            return 1

        max_ = max(nums)
        min_ = min(nums)
        choices = []

        idx1 = -1
        idx2 = -1

        for idx in range(L):
            if nums[idx] == max_:
                idx1 = idx

            if nums[idx] == min_:
                idx2 = idx

        choices.append(max(idx1, idx2) + 1)
        choices.append(L - min(idx1, idx2))
        if idx1 < idx2:
            choices.append(idx1 + 1 + L - idx2)

        else:
            choices.append(idx2 + 1 +  L - idx1)

        return min(choices)
