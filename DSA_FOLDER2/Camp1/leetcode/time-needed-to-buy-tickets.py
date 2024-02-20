class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        L = len(tickets)

        idx = 0
        wait = 0
        while tickets[k]  != 0:
            for idx in range(L):
                if tickets[idx] and tickets[k]:
                    tickets[idx] -= 1
                    wait += 1



        return wait