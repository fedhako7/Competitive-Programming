class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        L = len(senate)
        dire = deque()
        rad = deque()

        for idx in range(L):
            if senate[idx] == 'D':
                dire.append(idx)
        
            else:
                rad.append(idx)


        while dire and rad:
            if dire[0] < rad[0]:
                dire.append(L + dire.popleft())
                rad.popleft()

            else:
                rad.append(L + rad.popleft())
                dire.popleft()


        if dire:
            return 'Dire'

        return  'Radiant'
        