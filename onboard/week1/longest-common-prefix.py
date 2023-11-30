class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        chars = []
        idx = min(len(strs[0]), len(strs[-1]))
        for i in range(idx):
            if strs[0][i] != strs[-1][i]:
                break
            else:
                chars.append(strs[0][i])


        return ''.join(chars)