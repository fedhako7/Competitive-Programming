class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
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
        for idx in range(len(subsets)):
            subsets[idx] = tuple(sorted(subsets[idx]))
            
        subsets = set(subsets)
        return subsets
        
        