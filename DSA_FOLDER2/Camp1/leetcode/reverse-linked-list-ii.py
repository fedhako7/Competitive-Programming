# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        right -= left
        left -= 1
        curr = head
        while left:
            curr = curr.next
            prev = prev.next 
            left -= 1
        dummy2 = ListNode(0, curr)
        while right:
            temp = curr.next
            curr.next = curr.next.next
            temp.next = dummy2.next
            dummy2.next = temp
            right -= 1
        prev.next = dummy2.next
        return dummy.next