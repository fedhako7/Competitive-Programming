# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        countA = 0
        countB = 0

        curr = headA
        while curr:
            curr = curr.next
            countA += 1

        curr = headB
        while curr:
            curr = curr.next
            countB += 1

        currA = headA
        currB = headB 
        
        while countA > countB:
            currA = currA.next
            countA -= 1

        while countB > countA:
            currB = currB.next
            countB -= 1

        while currA and currB:
            if currA == currB:
                return currA

            currA = currA.next
            currB = currB.next

        return None



        