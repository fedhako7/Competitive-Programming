# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxDiameter = 0
        def findDiameter(root):
            nonlocal maxDiameter
            if not root:
                return 0

            left =  1 + findDiameter(root.left)
            right = 1 + findDiameter(root.right)
            maxDiameter = max(maxDiameter, left + right)

            return max(left, right)

        findDiameter(root)
        return maxDiameter - 2