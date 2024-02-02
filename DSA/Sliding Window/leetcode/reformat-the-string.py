class Solution:
    def reformat(self, s: str) -> str:
        digit = 0 
        letter = 0

        for char in s:
            if char.isdigit():
                digit += 1
            else:
                letter += 1

        if abs(letter - digit) > 1:
            return ''

        s_list = [0] * len(s)
        idx = 0
        for char in s:
            if idx < len(s) and letter >= digit and not char.isdigit():
                s_list[idx] = char
                idx += 2

            elif idx < len(s) and digit > letter and char.isdigit():
                s_list[idx] = char
                idx += 2
                
        idx = 1
        for char in s:
            if idx < len(s) and letter < digit and not char.isdigit():
                s_list[idx] = char
                idx += 2

            elif idx < len(s) and letter >= digit and char.isdigit():
                s_list[idx] = char
                
                idx += 2
        
        
        return ''.join(s_list)

