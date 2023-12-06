class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCandy = max(candies)
        bools = []
        for idx in range(len(candies)):
            kid_i = candies[idx] + extraCandies >= maxCandy
            bools.append(kid_i)
        return bools

        