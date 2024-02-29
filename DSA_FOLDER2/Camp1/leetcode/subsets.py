class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        subs = []
        def backT(index):
            if len(nums) == index:
                subsets.append(subs[:])
                return

            subs.append(nums[index])

            backT(index + 1)
            subs.pop()
            backT(index + 1)

        backT(0)
        return subsets
        