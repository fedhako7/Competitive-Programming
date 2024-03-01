class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        maxInRow = {}
        maxInCol = {}

        for idx, row in enumerate(grid):
            maxInRow[idx] = max(row)

        zipped_grid = zip(*grid) 

        for idx, col in enumerate(zipped_grid):
            maxInCol[idx] = max(col)

        newHeight = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                newHeight += min(maxInRow[r], maxInCol[c]) - grid[r][c]

        return newHeight