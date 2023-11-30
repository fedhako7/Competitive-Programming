class Solution:
    def checkPowersOfThree(self, n):
        while n:
            n, rem = divmod(n, 3)
            if rem == 2:
                return False
        return True