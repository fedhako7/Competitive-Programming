class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        oneRows = []

        for st in words:
            if self.isOneRow(st):
                oneRows.append(st)

        return oneRows


    #checks and returns True if s is in on row
    def isOneRow(self, s: str) -> bool:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        # Change s to lowercase in case it has Uppercase chars
        s = s.lower()

        # Checks if s is in first row
        if s[0] in rows[0]:
            for idx in range(1, len(s)):
                if s[idx] not in rows[0]:
                    return False

            return True

        # Checks if s is in second row
        elif s[0] in rows[1]:
            for idx in range(1, len(s)):
                if s[idx] not in rows[1]:
                    return False

            return True

        # Checks if s is in third row
        elif s[0] in rows[2]:
            for idx in range(1, len(s)):
                if s[idx] not in rows[2]:
                    return False

            return True