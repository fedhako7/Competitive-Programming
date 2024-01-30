class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        all_shifts = [0] * (len(s) + 1)
        s_list = list(s)

        for start, end, direc in shifts:
            if direc == 1:
                all_shifts[start] += 1
                all_shifts[end + 1] -= 1
            else:
                all_shifts[start] -= 1
                all_shifts[end + 1] += 1

        for idx in range(1, len(s)):
            all_shifts[idx] += all_shifts[idx - 1]

        for idx, char in enumerate(s_list):
            ord_ = (ord(char) - ord('a') + all_shifts[idx])
            ord_ %= 26

            if ord_ < 0:
                ord_ += 26
            
            s_list[idx] = chr(ord_ + ord('a'))


        return ''.join(s_list)