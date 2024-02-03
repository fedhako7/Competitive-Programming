# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head

        elif not head.next.next:
            return head.next


        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            fast = fast.next

        '''while slow:
            print(slow.val)
            slow'''
        return slow