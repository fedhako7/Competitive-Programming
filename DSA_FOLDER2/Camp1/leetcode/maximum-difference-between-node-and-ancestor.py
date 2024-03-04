# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxDiff = -inf

        def findMaxDiff(root, maxVal, minVal):
            nonlocal maxDiff
            if not root:
                return 

            minVal = min(root.val, minVal)
            maxVal = max(root.val, maxVal)
            maxDiff = max(maxDiff, maxVal - minVal)

            findMaxDiff(root.left, maxVal, minVal)
            findMaxDiff(root.right, maxVal, minVal)


        findMaxDiff(root, root.val, root.val)
        return maxDiff
