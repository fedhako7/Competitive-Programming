class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        L = len(prices)
        nextS = []

        for idx in range(L):
            while nextS and prices[idx] <= prices[nextS[-1]]:
                prices[nextS[-1]] -= prices[idx]
                nextS.pop()
        
            nextS.append(idx)

        return prices