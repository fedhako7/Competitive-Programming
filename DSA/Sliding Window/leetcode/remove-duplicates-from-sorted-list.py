# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev = head
        curr = prev.next

        while curr:
            if curr.val == prev.val:
                temp = curr
                prev.next = curr.next
                curr = curr.next
                del temp

            else:
                prev = prev.next
                if curr:
                    curr = curr.next

        return head


        