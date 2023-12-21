class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        mat_dic = collections.defaultdict(list)
        diagonals = []

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                mat_dic[row + col].append(mat[row][col])

        for key in mat_dic:
            if key % 2:
                diagonals += mat_dic[key]
            else:
                diagonals += reversed(mat_dic[key]) 

        return diagonals