class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        
        for idx in range(len(s)):
            if count[s[idx]] == 1:
                return idx

        return -1