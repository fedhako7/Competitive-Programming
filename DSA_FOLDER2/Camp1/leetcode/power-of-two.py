class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        elif n < 1 or n != int(n):
            return False

        return self.isPowerOfTwo(n / 2)
        