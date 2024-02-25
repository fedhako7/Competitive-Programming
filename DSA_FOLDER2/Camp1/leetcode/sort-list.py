# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = dummy
        count = 0
        nodes = {}
        curr = head

        while curr:
            nodes[count] = curr
            curr = curr.next
            count += 1

        keys = [k for k in nodes]
        keys.sort(key = lambda x: nodes[x].val)

        for key in keys:
            nodes[key].next = None
            tail.next = nodes[key]
            tail = tail.next

        return  dummy.next
