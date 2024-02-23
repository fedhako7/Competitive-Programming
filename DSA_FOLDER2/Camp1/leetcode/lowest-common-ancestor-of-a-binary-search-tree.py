# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if p.val < q.val:
            temp = p
            p = q
            q = temp 

        if q.val <= root.val <= p.val:
            return root

        elif p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        
       
        elif q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        
       


        