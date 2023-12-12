class Solution(object):
    def isHappy(self, n):
       # Trick is, if we don  get sum == 1, our sum is repeated after some point.
        numList = [] # List to track our curr sum, to handle sum repetition 
        while True:
            if n == 1:
                return True
            elif n in numList:
                return False
            else:
                numList.append(n)
            curr = 0
            for digit in str(n):
                curr += (int(digit)) ** 2
            n = curr
