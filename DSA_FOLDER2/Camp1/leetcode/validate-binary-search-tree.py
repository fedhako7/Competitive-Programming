# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def isValid(root, minVal, maxVal):
            if not root: 
                return True
            
            if not (minVal < root.val < maxVal):
                return False

            return (isValid(root.left, minVal, root.val) and isValid(root.right, root.val, maxVal))

        
        return isValid(root, -float("inf"), float("inf"))
        