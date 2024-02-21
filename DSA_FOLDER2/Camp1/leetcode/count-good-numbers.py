class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(x, y):
            if y == 0:
                return 1
          
            ans = power(x, y // 2)
            ans = (ans * ans) % (10**9+7)

            if y % 2 == 1:
                ans = ans * x %(10**9+7)
           
            return  ans


        mod = 10 ** 9 + 7
        even = n // 2 + (n % 2)
        odd = n // 2
        good = (power(5, even) % (mod) * power(4, odd) % (mod)) % mod
        return good