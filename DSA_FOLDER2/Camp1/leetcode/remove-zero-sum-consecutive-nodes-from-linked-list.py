# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        prefixSums = defaultdict(int)
        prefixSum = 0

        while curr:
            if curr.val != 0:
                arr.append(curr.val)

            curr = curr.next


        L = len(arr)
        for idx in range(L):
            prefixSum += arr[idx]

            if idx > 0 and prefixSum == 0:
                for i in range(idx + 1):
                    arr[i] = 0
                    prefixSums[i] = 0

            if prefixSum in dict(prefixSums).values():
                key = 0
                while prefixSums[key] != prefixSum:
                    key += 1

                for i in range(key + 1, idx + 1):
                    arr[i] = 0
                    prefixSums[i] = 0
                
            else:
                prefixSums[idx] = prefixSum


        dummy = ListNode()
        tail = dummy
        for idx in range(len(arr)):
            newNode = ListNode(arr[idx])
            if newNode.val != 0:
                tail.next = newNode
                tail = newNode


        return dummy.next