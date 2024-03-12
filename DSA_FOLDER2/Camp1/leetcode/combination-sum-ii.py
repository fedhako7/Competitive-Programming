class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #candidates.sort()
        print(len(candidates))
        allCombs = set()
        currCombs = []


        def findSum(idx):
            if sum(currCombs) == target:
                allCombs.add(tuple(sorted(currCombs)))

            if idx == len(candidates) or sum(currCombs) >= target:
                return 

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                currCombs.append(candidates[i]) 
                findSum(i + 1)
                currCombs.pop()


        findSum(0)
        return allCombs