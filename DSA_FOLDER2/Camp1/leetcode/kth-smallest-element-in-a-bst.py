# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        def trav(root):
            if not root:
                return 

            trav(root.left)
            stack.append(root.val)
            trav(root.right)

        trav(root)

        return (stack[k - 1])