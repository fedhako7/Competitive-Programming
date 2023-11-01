class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l, r = 0, math.sqrt(c) // 1
        if 2 * (l ** 2) > c or 2*(r ** 2) < c:
            return False

        while l <= r:
            if (l ** 2) + (r ** 2) == c:
                return True
            elif (l ** 2) + (r ** 2) < c:
                l += 1
            elif (l ** 2) + (r ** 2) > c:
                r -= 1

        return False
