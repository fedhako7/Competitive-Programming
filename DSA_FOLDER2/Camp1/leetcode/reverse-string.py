class Solution(object):
    def reverseString(self, s):
        #USING TWO POINTER
        '''
        l, r = 0, len(s) - 1
        while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
        '''

        #USING RECURSION
        def recurs(l, r):
            if l == r or l > r:
                return

            s[l], s[r] = s[r], s[l]

            recurs(l + 1, r - 1)


        recurs(0, len(s) - 1)