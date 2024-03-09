class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        L =len(weights)
        #Possible indices to split at
        splitPoints = []

        for idx in range(L - 1):
            splitPoints.append(weights[idx] + weights[idx + 1])


        splitPoints.sort()
        # Only k - 1 max and min scores are selected
        minScore = sum(sorted(splitPoints)[ :k - 1])
        maxScore = sum(sorted(splitPoints, reverse=True)[ :k - 1])
        print(splitPoints)

        return maxScore - minScore

        