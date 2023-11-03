class Solution(object):
    def maxTurbulenceSize(self, arr):
        '''
        [10>5<8>6]
        '''
        l, r = 0, 1
        ans, sign = 1, ''
        while r < len(arr):
            if arr[r - 1] > arr[r] and sign != '>':
                ans = max(ans, r - l + 1)
                r += 1
                sign = '>'
            elif arr[r - 1] < arr[r] and sign != '<':
                ans = max(ans, r - l + 1)
                r += 1
                sign = '<'
            else:
               r = r + 1 if arr[r] == arr[r - 1] else r
               l = r - 1
               sign = '='

        return ans
