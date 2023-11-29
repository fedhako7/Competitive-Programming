class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        l, r = 0, len(x) - 1
        while l <= r:
            if x[l] != x[r]:
                return False
            l += 1
            r -= 1
        return True

        