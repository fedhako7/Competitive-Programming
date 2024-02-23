class Solution:
    def numberOfSteps(self, num: int) -> int:

        step = 0
        while num:
            if num % 2 == 1:
                num -= 1
                step += 1

            if num:
                num /= 2
                step += 1

        return step
        
        