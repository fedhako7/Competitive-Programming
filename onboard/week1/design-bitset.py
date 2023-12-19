class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.one_set =  set()
        self.zero = {idx for idx in range(self.size)}
        

    def fix(self, idx: int) -> None:
        self.one_set.add(idx)
        self.zero.discard(idx)
        

    def unfix(self, idx: int) -> None:
        self.one_set.discard(idx)
        self.zero.add(idx)
        

    def flip(self) -> None:
        temp = self.one_set
        self.one_set = self.zero
        self.zero = temp

        

    def all(self) -> bool:
        check = len(self.one_set) == self.size
        return check

    def one(self) -> bool:
        check = len(self.one_set) > 0
        return check
        

    def count(self) -> int:
        count = len(self.one_set) 
        return count
        

    def toString(self) -> str:
        string = []
        for i in range(self.size):
            string.append('1') if i in self.one_set else string.append('0')

        return ''.join(string)

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()