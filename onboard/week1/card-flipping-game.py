class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        good = float('inf')
        always_up = []
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                always_up.append(fronts[i])

        for i in range(len(fronts)):
            max_ = max(fronts[i], backs[i])
            min_ = min(fronts[i], backs[i])
            if min_ not in always_up:
                good = min(good, min_)

            elif max_ not in always_up:
                good = min(good, max_)


        return good if good != float('inf') else 0        

        