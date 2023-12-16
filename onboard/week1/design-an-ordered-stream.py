class OrderedStream:
    def __init__(self, n: int):
        self.ptr = 0
        self.values = [None] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.values[idKey] = value
        if idKey > self.ptr:
            return []

        chunks = []    
        while self.ptr < len(self.values) and self.values[self.ptr]:
            chunks.append(self.values[self.ptr])
            self.ptr += 1

        return chunks