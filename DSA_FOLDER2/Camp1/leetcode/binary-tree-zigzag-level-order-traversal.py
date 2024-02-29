# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        levelVals = defaultdict(list)
        def zigzag(root, key):
            if not root:
                return 

            levelVals[key].append(root.val)
            zigzag(root.left, key + 1)
            zigzag(root.right, key + 1)


        zigzag(root, 0)
        for key in dict(levelVals).keys():
            if key % 2:
                levelVals[key].reverse() 

        return dict(levelVals).values()
            