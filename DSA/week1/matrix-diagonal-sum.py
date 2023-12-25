class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primary_diag_sum = 0

        row = 0 
        while row < len(mat):
            primary_diag_sum += mat[row][row] 
            mat[row][row] = 0 
            row += 1

        col = 0
        row -= 1
        while col < len(mat):
            primary_diag_sum += mat[row][col]
            col += 1
            row -= 1

        return primary_diag_sum 








