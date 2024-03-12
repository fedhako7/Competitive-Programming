class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

        def findSum(idx):

            if sum(curr) == target:
                allSum.append(curr[:])


            if idx == len(candidates) or sum(curr) >= target:
                return


            curr.append(candidates[idx])
            findSum(idx)
            curr.pop()
            findSum(idx + 1)

        allSum = []
        curr = []
        findSum(0)
        return allSum
