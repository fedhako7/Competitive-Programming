# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def delete(root, key):
            if not root:
                return None


            if root.val > key:
                root.left = delete(root.left, key)
                return root


            elif root.val < key:
                root.right = delete(root.right, key)
                return root

            else:
                if not root.left:
                    return root.right

                elif not root.right:
                    return root.left

                cur = root.right

                while cur.left:
                    cur = cur.left

                root.val = cur.val
                root.right = delete(root.right, root.val)
                return root


        return delete(root, key)

            

            
        
        