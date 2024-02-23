class Solution:                         
    def minMoves(self, target: int, maxDoubles: int) -> int:

        moves = 0

        while target > 1:
            if not maxDoubles:
                moves += (target - 1)
                target = 1

            else:
                if target % 2 == 1:
                    target -= 1
                    moves += 1


                target /= 2                               
                maxDoubles -= 1                           
                moves += 1                                


        
        return int(moves)
            
