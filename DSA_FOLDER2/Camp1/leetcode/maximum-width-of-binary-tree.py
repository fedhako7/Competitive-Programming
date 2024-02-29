# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic = defaultdict(list)

        def dfs(root, level, key):
            if not root:
                return 


            dic[level].append(key)
            dfs(root.left, level + 1, key * 2)
            dfs(root.right, level + 1, key * 2 + 1)

        

        dfs(root, 0, 1)
        maxWid = 1
        for node in dic:
            if len(dic[node]) > 1:
                maxWid = max(maxWid, dic[node][-1] - dic[node][0] + 1)

        return maxWid












        