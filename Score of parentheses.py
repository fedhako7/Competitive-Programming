class Solution(object):
    def scoreOfParentheses(self, s):
        op = []
        for a in s:
            if a == '(':
                op.append(a)
            elif a == ')':
                last_item = op.pop()                         
                if last_item == '(':
                    op.append(1)
                else:
                    op[-1] = last_item * 2
            if len(op) >= 2:
                if isinstance(op[-1], int) and isinstance(op[-2], int):
                    op.append(op.pop() + op.pop())

        return op[0]
