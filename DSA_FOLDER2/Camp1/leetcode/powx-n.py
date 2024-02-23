class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def powe(x, n):
            if n == 0:
                return 1

            ans = powe(x, n // 2)
            ans *= ans
            if n % 2:
                ans *= x

            return ans


        
        powRes = powe(abs(x), abs(n))
        if n < 0:
            powRes = 1 / powRes

        if x < 0 and abs(n) % 2:
            powRes *= -1

        return powRes
            