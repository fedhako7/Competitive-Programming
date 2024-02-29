class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.stack = []
        

    def enQueue(self, value: int) -> bool:
        L = len(self.stack)

        if L < self.size:
            self.stack.append(value)
            return True
        
        return False

    def deQueue(self) -> bool:
        if self.stack:
            self.stack = self.stack[1:]
            return True

        return False
        

    def Front(self) -> int:
        if self.stack:
            return self.stack[0]

        return -1
        

    def Rear(self) -> int:
        if self.stack:
            return self.stack[-1]

        return -1
        

    def isEmpty(self) -> bool:
        return len(self.stack) == 0
        

    def isFull(self) -> bool:
        return len(self.stack) == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()