# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        tort, rab = head, head
        while rab and rab.next:
            if not rab or not rab.next:
                return False


            tort = tort.next
            rab = rab.next.next
        
            if rab == tort:
                return True