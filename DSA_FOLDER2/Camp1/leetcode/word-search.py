class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:



        def findWord(row, col, idx):
            nonlocal word
            if idx == len(word):
                return True
            
            if (row < 0 or row >= len(board) or col < 0 or col >= len(board[0])):
                return False

            if word[idx] != board[row][col] or (row, col) in path:
                return False

            path.add((row, col))
            found = (findWord(row + 1, col, idx + 1) or
                    findWord(row, col + 1, idx + 1) or
                    findWord(row - 1, col, idx + 1) or
                    findWord(row, col - 1, idx + 1))
            
            path.remove((row, col))
            return found


        path = set()
        for row in range(len(board)):
            for col in range(len(board[0])):

                if findWord(row, col, 0):
                    return True

        return False