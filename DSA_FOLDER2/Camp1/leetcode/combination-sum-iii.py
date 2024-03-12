class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > 45:
            return []
        
        
        def findSum(idx):
            if len(currComb) == k and sum(currComb) == n:
                allComb.append(currComb[:])

            if len(currComb) > k or sum(currComb) > n or idx == 10:
                return 

            for i in range(idx, 10):
                currComb.append(i)
                findSum(i + 1)
                currComb.pop()


        allComb = []
        currComb = []
        findSum(1)
        return allComb
        