class Solution:
    def numberOfWays(self, s: str) -> int:
        left_zero = 0
        left_one = 0
        prefixes = [0] * len(s)
        for idx in range(len(s)):
            if s[idx] == '0':
                prefixes[idx] = left_one
                left_zero += 1

            else:
                prefixes[idx] = left_zero
                left_one += 1

        
        right_one = 0
        right_zero = 0
        for idx in range(len(s) - 1, -1, -1):
            if s[idx] == '0':
                prefixes[idx] *= right_one
                right_zero += 1

            else:
                prefixes[idx] *= right_zero
                right_one += 1
            

        way = 0
        for choice in prefixes:
            way += choice

        return way




         