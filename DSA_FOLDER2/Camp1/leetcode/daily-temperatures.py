class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        L = len(temps)
        answer = [0] * L
        nextW = []

        for idx in range(L):
            while nextW and temps[idx] > temps[nextW[-1]]:
                answer[nextW[-1]] = idx - nextW[-1]
                nextW.pop()

            nextW.append(idx)
            print

        return answer