class Solution(object):
    def sumOfThree(self, num):
        if num % 3 != 0:
            return []
        else:
            return [num  / 3 - 1, num / 3, num / 3 + 1]
        