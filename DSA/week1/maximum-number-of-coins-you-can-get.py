class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        piles.sort()

        return sum(piles[n // 3::2])
        