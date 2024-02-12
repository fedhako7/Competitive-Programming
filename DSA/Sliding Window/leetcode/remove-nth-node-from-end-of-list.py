# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        prevNode = head

        while end.next:
            end = end.next
            n -= 1

            if n < 0:
                prevNode = prevNode.next

        if n == 1:
            if prevNode.next:
                head = prevNode.next
                del prevNode
                return head
            
            del head
            return None
                
        if prevNode.next:
            temp = prevNode.next
            prevNode.next = prevNode.next.next
            del temp

            return head

        
        
        

