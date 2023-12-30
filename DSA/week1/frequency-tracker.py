class FrequencyTracker:

    def __init__(self):
        self.data = collections.defaultdict(int)
        self.freq = collections.defaultdict(int)

    def add(self, number: int) -> None:
        prev = self.data[number]
        
        self.data[number] += 1
        self.freq[prev] -= 1
        self.freq[prev + 1] += 1

    def deleteOne(self, number: int) -> None:
        prev = self.data[number]

        if prev != 0:
            
            self.data[number] -= 1
            self.freq[prev] -= 1
            self.freq[prev - 1] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)