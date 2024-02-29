class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(0)
        L = len(arr)
        tot = 0

        countLeftG = [0] * L
        indices = []
        for idx in range(L):
            while indices and arr[idx] < arr[indices[-1]]:
                idx2 = indices[-1]
                tot += (arr[idx2] * countLeftG[idx2] * (idx - idx2))
                tot %= (10 ** 9 + 7)
                indices.pop()

            countLeftG[idx] = (idx - indices[-1]) if indices else (idx + 1)
            indices.append(idx)

        print(countLeftG)
        return tot