# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root):
        
        def backT(node):
            if not node: return []
            return backT(node.left) + [node.val] + backT(node.right)
        ns = backT(root)
        
        def build(left, right):
            if left > right: return None
            m = (left + right) // 2
            root = TreeNode(ns[m])
            root.left, root.right = build(left, m-1), build(m + 1, right)
            return root
        
        return build(0, len(ns) - 1)