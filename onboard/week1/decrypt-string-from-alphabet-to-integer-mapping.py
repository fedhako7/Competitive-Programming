class Solution(object):
    def freqAlphabets(self, s):
        answer = ''
        for idx in range(len(s) - 2):
            if s[idx] == '#' or s[idx + 1] == '#':
                continue
            elif s[idx + 2] == '#':
                answer = answer + chr(int(s[idx:idx+2]) + 96)
            else:
                answer = answer + chr(int(s[idx]) + 96)
        if s[-1] != '#':
            answer = answer + chr(int(s[-2]) + 96) if s[-2] != '#' else answer
            answer = answer + chr(int(s[-1]) + 96)
        return answer
