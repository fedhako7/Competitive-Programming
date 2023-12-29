class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0: return 0
        positive = True if num > 0 else False
        num = str(num) if positive else str(num)[1: ]

        len_zero = 0 
        for digit in num:
            if digit == '0':
                len_zero += 1

        num = [n for n in num if n != '0']

        # If a given number is a positive 
        if positive:
            def compar(dig1, dig2):   # Helper function for positive number
                if dig1 + dig2 < dig2 + dig1:
                    return -1

                elif dig1 + dig2 > dig2 + dig1:
                    return 1

                else:
                    return 0


            num.sort(key = cmp_to_key(compar))
            num = list(num[0]) + (['0'] * len_zero) + (num[1:])
        # If a given number is negative
        else:
            def compar_negative(dig1, dig2): # Helper for negative numbers
                if dig1 + dig2 > dig2 + dig1:
                    return -1
                elif dig1 + dig2 < dig2 + dig1:
                    return 1
                else:
                    return 0

            num.sort(key = cmp_to_key(compar_negative))

            num = ['-'] + num + (['0'] * len_zero)

        return int(''.join(num))

        
