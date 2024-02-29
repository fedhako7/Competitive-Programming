# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:


        def isMir(root1, root2):
            if not root1 and not root2:
                return True

            if not root2 or not root1:
                return False
                
            return (root1.val == root2.val and
                    isMir(root1.left, root2.right) and
                    isMir(root1.right, root2.left))


        return isMir(root.left, root.right)