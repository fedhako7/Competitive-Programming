class Solution:
    def isValid(self, s: str) -> bool:
        L = len(s)
        opens = []

        for brac in s:
            if brac in '({[':
                opens.append(brac)

            elif opens and brac == ')' and opens[-1] == '(':
                opens.pop()
            elif opens and brac == '}' and opens[-1] == '{':
                opens.pop()
            elif opens and brac == ']' and opens[-1] == '[':
                opens.pop()

            else:
                return False


        return (not opens)