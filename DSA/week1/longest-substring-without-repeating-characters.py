class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        for l in range(len(s)):
            checkList = []
            r = l

            while r < len(s) and s[r] not in checkList:
                checkList.append(s[r])
                r += 1
            tempLen = r - l
            if tempLen > ans:
                ans = tempLen

        return ans

        