class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        k = len(s1)
        count_s1 = Counter(s1)

        count_s2 = Counter(s2[ :k])

        if count_s1 == count_s2:
            return True


        for idx in range(k, len(s2)):
            count_s2[s2[idx]] += 1
            count_s2[s2[idx - k]] -= 1

            if count_s2[s2[idx - k]] == 0:
                del count_s2[s2[idx - k]]

            if count_s1 == count_s2:
                return True

        return False

