class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = [0] * 1001
        max_initial = float('-inf')

        for passen, initial, terminal in trips:
            passengers[initial] += passen
            passengers[terminal] -= passen
            max_initial = max(max_initial, initial)

        if passengers[0] > capacity:
            return False


        for idx in range(1, max_initial + 1):
            passengers[idx] += passengers[idx - 1]

            if passengers[idx] > capacity:
                return False

        return True

        