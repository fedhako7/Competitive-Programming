class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if s.count(' ') + 1 != len(pattern):
            return False

        dic = {}

        s1 = s.split()[ :len(pattern)]
        print(s)

        for idx, c in enumerate(pattern):
            print(idx)
            if c not in dic:
                dic[c] = s1[idx]

            elif dic[c] != s1[idx]:
                return False


        dic2 = {}

        s2 = s.split()[ :len(pattern)]
        print(s)

        for idx, c in enumerate(s2):
            print(idx)
            if c not in dic2:
                dic2[c] = pattern[idx]

            elif dic2[c] != pattern[idx]:
                return False
    

        return True
