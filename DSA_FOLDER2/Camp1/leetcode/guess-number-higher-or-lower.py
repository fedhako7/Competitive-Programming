# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        low = 0
        high = n + 1
        
        while low + 1 < high:
            mid = (low + high) // 2

            pick = guess(mid)
            if pick == 0:
                return mid

            elif pick == 1:
                low = mid
                
            else:
                high = mid