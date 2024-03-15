class Solution:
    def mySqrt(self, x: int) -> int:

        low = 0
        high = x + 1

        while low + 1 < high:
            mid = (low + high) // 2

            if mid ** 2 > x:
                high = mid

            else:
                low = mid

        return low

        