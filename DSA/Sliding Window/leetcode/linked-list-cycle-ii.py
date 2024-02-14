# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        tort = head
        rab = head
        while rab:
            if not rab.next or not rab.next.next:
                return

            tort = tort.next
            rab = rab.next.next
            if rab == tort:
                break
       

        rab = head
        while rab != tort:
            
            rab = rab.next
            tort = tort.next

        return rab
        