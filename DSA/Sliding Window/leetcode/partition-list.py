# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        small = ListNode()
        sTail = small

        great = ListNode()
        gTail = great

        curr = head
        while curr:
            temp = curr.next
            if curr.val < x:
                curr.next = None
                sTail.next = curr
                sTail = sTail.next

            else:
                curr.next = None
                gTail.next = curr
                gTail = gTail.next

            curr = temp

        if sTail:
            sTail.next = great.next

        return small.next

        