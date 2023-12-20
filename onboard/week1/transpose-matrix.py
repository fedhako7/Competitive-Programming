class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        
        for col in range(len(matrix[0])):
            t_row = []
            for row in range(len(matrix)):
                t_row.append(matrix[row][col])

            transpose.append(t_row)

        return transpose