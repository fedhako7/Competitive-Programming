class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROW, COL = len(matrix), len(matrix[0])
        self.sum_mat = [[0] * (COL + 1) for _ in range(ROW + 1)]

        for r in range(ROW):
            prefix = 0
            for c in range(COL):
                prefix += matrix[r][c]
                above = self.sum_mat[r][c + 1]

                self.sum_mat[r + 1][c + 1] = prefix + above

        print(self.sum_mat)


    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        r1, r2, c1, c2 = r1 + 1, r2 + 1, c1 + 1, c2 + 1 

        bottom_right = self.sum_mat[r2][c2]
        top = self.sum_mat[r1 - 1][c2]
        left = self.sum_mat[r2][c1 - 1]
        doubled = self.sum_mat[r1 - 1][c1 - 1]


        return bottom_right - top - left + doubled

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)