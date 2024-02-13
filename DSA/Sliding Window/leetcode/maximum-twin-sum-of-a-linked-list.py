# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        node = head

        while node:
            arr.append(node.val)
            node = node.next

        maxSum = 0
        currSum = 0
        left, right = 0, len(arr) - 1
        while left < right:
            currSum = (arr[left] + arr[right])
            maxSum = max(maxSum, currSum)
            left += 1
            right -= 1

        return maxSum