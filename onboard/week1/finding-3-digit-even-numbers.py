class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        integers = []
        digits = collections.Counter(digits)
        num = 100

        while num < 999:
            digit = str(num)

            if int(digit[0]) not in digits:
                num += 100
            elif int(digit[1]) not in digits:
                num += 10
            elif int(digit[2]) not in digits:
                num += 2
            else:
                for dgt in digit:
                    if digit.count(dgt) > digits[int(dgt)]:
                        break
                else:   
                    integers.append(num)

                num += 2

        return integers