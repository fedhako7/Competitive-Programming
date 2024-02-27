class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        def validParen(s):
            if s.count('(') != s.count(')'):
                return False

            open = 0
            close = 0
            for br in s:
                if br == '(':
                    open += 1
                elif br == ')':
                    if open:
                        open -= 1
                    else:
                        return False
            return open == 0


        paren = []
        s = []
        def backT(size):
            if size == 2 * n:
                if validParen(s):
                    paren.append(''.join(s[:]))
                return
            s.append('(')
            backT(size + 1)
            s.pop()
            s.append(')')
            backT(size + 1)
            s.pop()


        backT(0)
        return paren



