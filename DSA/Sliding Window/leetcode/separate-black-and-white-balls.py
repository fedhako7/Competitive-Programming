class Solution:
    def minimumSteps(self, s: str) -> int:
        curr_white = 0
        step = 0

        right = len(s) - 1
        for idx in range(len(s) - 1, -1, -1):
            if s[idx] == '0':
                curr_white += 1
            elif s[idx] == '1':
                step += curr_white

        
        return step