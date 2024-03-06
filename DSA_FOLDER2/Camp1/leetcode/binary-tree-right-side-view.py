# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:


        nodes = defaultdict(list)
        rightSide = []
        def rightView(root, depth):
            if not root:
                return 
            nodes[depth].append(root.val)
            rightView(root.left, depth + 1)
            rightView(root.right, depth + 1)


        rightView(root, 0)
        for depth in nodes:
            rightSide.append(nodes[depth][-1])

        return rightSide
                


