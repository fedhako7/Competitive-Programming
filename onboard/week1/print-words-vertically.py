class Solution(object):
    def printVertically(self, s):
        hor = s.split(' ')
        ver = []
        maxLen = len(max(hor, key = len))
        idx = 0

        while idx < maxLen:
            v = ''
            
            for st in hor:
                if idx >= len(st):
                    v = v + ' '
                else:
                     v = v + st[idx]

            ver.append(v.rstrip())
            idx += 1

        return ver



















        