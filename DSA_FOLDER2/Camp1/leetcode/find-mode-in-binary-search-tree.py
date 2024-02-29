# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)

        def trav(root):
            if not root:
                return 

            count[root.val] += 1
            trav(root.left)
            trav(root.right)

        trav(root)
        print(dict(count))

        keys = sorted(dict(count).keys(), key = lambda x: count[x])
        mode = count[keys[-1]]
        print(mode)
        modes = [m for m in keys if count[m] == mode]
        return modes