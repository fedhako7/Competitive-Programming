# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = []
      
        def add(root, s):
            s.append(str(root.val))

            if not root.left and not root.right:
                stack.append("".join(s))
                s.pop()
                return
            
            if root.left:
                add(root.left, s)

            if root.right:
                add(root.right, s)
            
            s.pop()


        add(root, [])

        print(stack)
        tot = 0
        for s in stack:
            tot += int(s)
        
        return tot
