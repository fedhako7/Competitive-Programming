class Solution(object):
    def interpret(self, command):
        stack = []
        for idx, char in enumerate(command):
            if char == 'G':
                stack.append('G')
            elif (idx < len(command) - 1) and char == '(':
                if command[idx + 1] == ')':
                    stack.append('o')
                else:
                    stack.append('al')
        return ''.join(stack)
        