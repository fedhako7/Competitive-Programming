class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        hrglass = 0

        for row in range(1, len(grid) - 1):
            for col in range(1, len(grid[0]) - 1):
                row1_sum = grid[row-1][col-1] + grid[row-1][col] + grid[row-1][col+1]
                row2_sum = grid[row][col]
                row3_sum = grid[row+1][col-1] + grid[row+1][col] + grid[row+1][col+1]
                rows_sum = row1_sum + row2_sum + row3_sum
                hrglass = max(hrglass, rows_sum)

        return hrglass






        #grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]] =   30
        #grid = [[1,2,3],[4,5,6],[7,8,9]]   = 35
        '''
            [1,2,3],   r=0 c=012
            [4,5,6],    r=1 c=1
            [7,8,9]]    r=2 c=012
                [6,2,1,3],  r=0 c=012  c=123
                [4,2,1,5],  r=1 c=
                [9,2,8,7],  r=2 c=
                [4,1,2,9]   r=3 c=

                row in range(1,lenMatrics-1):
                    for col in range(1, lenM[row] - 1):
                        r1,r2,r3 = row, row-1, row+1
                        c1,c2,c3= col, col-1, col+1
                        
                        sum_=sum(M[r2,c2], M[r2,c1], M[r2, c3], M[r1,c1], M[r3, c2], M[r3, c1],M[r3,c1])

                        hourglass = max(hrg, sum_)
            '''