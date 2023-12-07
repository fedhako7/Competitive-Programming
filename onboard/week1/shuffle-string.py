class Solution(object):
    def restoreString(self, s, indices):
        shuffle = [''] * len(s)

        for i in range(len(s)):
            shuffle[indices[i]] = s[i]

        return ''.join(shuffle)