# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #BY ITERATION
        '''if not list1:
            return list2
        if not list2:
            return list1

        dummy = ListNode()
        tail = dummy
        curr1, curr2 = list1, list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next
        
        if curr1: 
            tail.next = curr1
        if curr2:
            tail.next = curr2
        return dummy.next'''

        # BY RECURSION

        if not list1 and not list2:
            return None

        elif not list1:
            return list2

        elif not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1

        else:
            list2.next = self.mergeTwoLists(list1, list2.next)

            return list2