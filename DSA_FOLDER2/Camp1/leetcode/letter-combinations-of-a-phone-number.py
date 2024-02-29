class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        buttons = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }


        chars = []
        curr = []
        def backT(given):
            if len(curr) == len(digits):
                if curr:
                    chars.append(''.join(curr))
                return
           
            for idx in range(len(given)):
                digt = given[idx]
                for char in buttons[digt]:
                    curr.append(char)
                    backT(given[idx + 1:])
 
                    curr.pop()

        backT(digits)
        return chars















