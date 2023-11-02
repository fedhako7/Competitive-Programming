class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1 = sorted(s1)
        k = len(s1)
        for l in range(len(s2)- k + 1):
            split = sorted(s2[l:l+k])
            if split == s1:
                return True

        return False
