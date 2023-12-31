class RandomizedSet:

    def __init__(self):
        self.set = set()
        self.dict = collections.defaultdict(int)
        

    def insert(self, val: int) -> bool:
        not_in = self.dict[val] == 0

        self.dict[val] = 1
        self.set.add(val)

        return not_in

        

        

    def remove(self, val: int) -> bool:
        was_in = self.dict[val] == 1
    
        self.dict[val] = 0
        self.set.discard(val)

        return was_in

    def getRandom(self) -> int:
       temp = self.set.pop()
       self.set.add(temp)
       return random.choice(tuple(self.set))



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()