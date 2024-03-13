class Solution:
    def longestNiceSubstring(self, s: str) -> str:


        def checkNice(s):
            if not s:
                return ''

            exists = set(s)

            for idx, char in enumerate(s):
                if (char.upper() not in exists) or (char.lower() not in exists):
                    return max(checkNice(s[ :idx]), checkNice(s[idx + 1: ]), key=len)

            else:
                return s

        
        return checkNice(s)
