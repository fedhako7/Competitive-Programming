class Node:
    def __init__(self, time = 0, next = None):
        self.time = time
        self.next = next




class RecentCounter:

    def __init__(self):
       self.dummy = Node()
       self.tail = self.dummy
       self.size = 0
        

    def ping(self, t: int) -> int:
        call = Node(t)
        self.tail.next = call
        self.tail = self.tail.next
        self.size += 1
        
        curr = self.dummy.next
        while curr and t - 3000 > curr.time:
            temp = curr.next
            self.dummy.next = temp
            del curr
            curr = temp
            self.size -= 1

        return self.size


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)