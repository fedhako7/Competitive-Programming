class Solution(object):
    def evalRPN(self, tokens):

        nums = []
        for elem in tokens:
            if elem not in "+-*/":
                nums.append(elem)
            elif elem == '+':
                op1 = int(nums.pop())
                op2 = int(nums.pop())
                nums.append(op1 + op2)

            elif elem == '-':
                op1 = int(nums.pop())
                op2 = int(nums.pop())
                nums.append(op2 - op1)
            elif elem == '*':
                op1 = int(nums.pop())
                op2 = int(nums.pop())
                nums.append(op1 * op2)
            elif elem == '/':
                op1 = int(nums.pop())
                op2 = int(nums.pop())
                nums.append(int(op2/float(op1)))

        return int(nums[0])
            
