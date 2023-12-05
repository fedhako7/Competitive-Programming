class Solution(object):
    def multiply(self, num1, num2):
        """
        {'0' = 0}
        create hashmap, whith digitchar key and digit as value
        reverse each digitstrint
        declare int_num1 and int_num2 whith = 0
        for enumaratr dstring, add add toDigitHashmap at digit multiplied 10 rised to idx
        same for num2
        return int_num1 * int_num2
        """
        strings_value = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        num1 = num1[: : -1]
        num2 = num2[: : -1]
        num1_value = 0
        num2_value = 0

        for idx, digit in enumerate(num1):
            num1_value += strings_value[digit] * (10 ** idx)

        for idx, digit in enumerate(num2):
            num2_value += strings_value[digit] * (10 ** idx)

        return str(num1_value * num2_value)


        