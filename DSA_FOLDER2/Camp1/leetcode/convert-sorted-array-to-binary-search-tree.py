# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def convert(nums):
            if len(nums) == 0:
                return None

            middle = ceil((len(nums) - 1) / 2)
            val = nums[middle]
            newNode = TreeNode(val)
            newNode.left = convert(nums[ :middle])
            newNode.right = convert(nums[middle + 1: ])

            return newNode

        return convert(nums)
        