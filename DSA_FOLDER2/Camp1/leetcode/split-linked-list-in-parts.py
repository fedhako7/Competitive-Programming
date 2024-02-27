# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        dummy = ListNode(0, head)
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1


        curr = dummy
        parts = 0
        nodesInPart = count // k
        nodes = []
        while parts < k:
            currLen = 0
            while currLen < nodesInPart:
                curr = curr.next
                currLen += 1

            if count % k:
                curr = curr.next
                count -= 1
            temp = None
            if curr:
                temp = curr.next
                curr.next = None
            nodes.append(dummy.next)
            dummy.next = temp
            curr = dummy
            parts += 1
        return nodes
            












