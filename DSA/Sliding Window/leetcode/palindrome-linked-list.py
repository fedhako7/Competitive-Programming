# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []

        node = head
        while node:
            arr.append(node.val)
            node = node.next

        return (arr == arr[::-1])