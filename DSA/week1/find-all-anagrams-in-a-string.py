class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_p = Counter(p)
        count_s = Counter(s[ :len(p)])
        equals = []

        if count_p == count_s:
            equals.append(0)

        for i in range(len(p), len(s)):
            count_s[s[i - len(p)]] -= 1
            count_s[s[i]] += 1
            if count_s[s[i - len(p)]] == 0:
                del count_s[s[i - len(p)]]

            if count_s == count_p:
                equals.append(i - len(p) + 1)
        return equals