class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, floor(sqrt(c))

        while left <= right:
            if (left ** 2) + (right ** 2) == c:
               return True

            elif (left ** 2) + (right ** 2) < c:
                left += 1

            else:
                right -= 1

        return False