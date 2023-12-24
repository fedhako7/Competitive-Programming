class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            r = [digit for digit in row if digit != '.']
            if len(set(r)) != len(r):
                print('loop1')
                return False
        
        for col in range(9):
            colum = []
            for row in range(9):
                if board[row][col] != '.':
                    colum.append(board[row][col])

            if len(set(colum)) != len(colum):
                return False
        
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):

                sub_boxes = []
                for i in range(3):
                    for j in range(3):
                        if board[r + i][c + j] != '.':
                            sub_boxes.append(board[r + i][c + j])

                if len(set(sub_boxes)) != len(sub_boxes):
                    return False

        return True




        