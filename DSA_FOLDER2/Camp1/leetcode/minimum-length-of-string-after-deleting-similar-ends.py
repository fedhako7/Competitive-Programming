class Solution:
    def minimumLength(self, s: str) -> int:
        L = len(s)
        newLen = L

        l, r = 0, L - 1
        while l < r:
            if newLen in [0, 1] or s[l] != s[r]:
                return newLen

            elif s[l] == s[r]:
                char = s[l]
                while l <= r and s[l] == char:
                    newLen -= 1
                    l += 1

                while r >= l and s[r] == char:
                    newLen -=1
                    r -= 1

            


        return newLen
        


        