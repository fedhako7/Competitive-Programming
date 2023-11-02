class Solution:
    def compress(self, chars):
        ptrL, ptrR = 0, 0
        total = 0
        chars += " "

        while ptrR < len(chars):
            if chars[ptrL] != chars[ptrR]:
                chars[total] = chars[ptrL]
                total += 1
                group = ptrR - ptrL
                if group > 1:
                    for x in str(group):
                        chars[total] = x
                        total += 1
                ptrL = ptrR
            ptrR += 1
            
        return total
