# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
            
        odd = ListNode()
        otail = odd
        even = ListNode()
        etail = even

        curr = head
        while curr:
            temp = curr.next
            curr.next = None
            otail.next = curr
            otail = otail.next
            if temp:
                curr = temp.next
            else:
                curr = None
            if temp:
                temp.next = None 
                etail.next = temp
                etail = etail.next

          
                
        
        otail.next = even.next
        return odd.next    