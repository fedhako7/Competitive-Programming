class Solution(object):
    def romanToInt(self, s):
        integer = 0
        for idx, r in enumerate(s): #"MCMXCIV"  1000
            num = 0
            if r == 'I':
                num = -1 if (idx <= len(s) - 2) and (s[idx + 1] == 'V' or s[idx + 1] == 'X') else 1
            elif r == 'V':
                num = 5
            elif r == 'X':
                num = -10 if (idx <= len(s) - 2) and (s[idx + 1] == 'L' or s[idx + 1] == 'C') else 10
            elif r == 'L':
                num = 50
            elif r == 'C':
                num = -100 if (idx <= len(s) - 2) and (s[idx + 1] == 'D' or s[idx + 1] == 'M') else 100
            elif r == 'D':
                num = 500
            elif r == 'M':
                num = 1000
            integer += num
        return integer