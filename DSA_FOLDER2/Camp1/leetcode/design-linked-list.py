class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
        

    def get(self, index: int) -> int:
        curr = self.dummy.next
        if curr: print(curr.val)
        while index and curr:
            print(curr.val)
            curr = curr.next
            index -= 1

        if curr:
            return curr.val

        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.dummy.next)
        self.dummy.next = node


    def addAtTail(self, val: int) -> None:
        node = Node(val)
        curr = self.dummy.next
        prev = self.dummy

        while curr:
            curr = curr.next
            prev = prev.next

        prev.next = node
        

    def addAtIndex(self, index: int, val: int) -> None:
        node = Node(val)
        curr = self.dummy
        while index and curr:
            curr = curr.next
            index -= 1
        
        if curr:
            node.next = curr.next
            curr.next = node


    def deleteAtIndex(self, index: int) -> None:
        curr = self.dummy.next
        prev = self.dummy

        while index and curr:
            curr = curr.next
            prev = prev.next
            index -= 1

        if curr:
            prev.next = curr.next
            del curr


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)