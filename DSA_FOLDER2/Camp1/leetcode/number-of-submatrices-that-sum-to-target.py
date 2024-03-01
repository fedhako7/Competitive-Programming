class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        R, C = len(matrix) + 1, len(matrix[0]) + 1

        matPrefix = [[0] * (C) for row in range(R)]
        for r in range(1, R):
            for c in range(1, C):
                leftPre = matPrefix[r][c - 1]
                topPre = matPrefix[r - 1][c]
                doubled = matPrefix[r - 1][c - 1]

                matPrefix[r][c] = matrix[r - 1][c - 1] + leftPre + topPre - doubled


        for r in range(R):
            print(matPrefix[r])

        subNum = 0
        for row1 in range(1, R):
            for row2 in range(row1, R):
                freq = defaultdict(int)
                freq[0] = 1
                for col in range(1, C):

                    currPre = matPrefix[row2][col] - (
                        matPrefix[row1 - 1][col] if row1 else 0
                        )


                    subNum += freq[currPre - target]
                    freq[currPre] += 1 

        return subNum










