class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sortDeck = sorted(deck)


        deckDeque = deque(deck)
        revealed = []
        while deckDeque:
            first = deckDeque.popleft()
            revealed.append(first)
            if deckDeque:
                other = deckDeque.popleft()
                if deckDeque:
                    deckDeque.append(other)
                else:
                    revealed.append(other)



        position = {}
        for idx in range(len(revealed)):
            position[revealed[idx]] = sortDeck[idx]


        for idx in range(len(deck)):
            deck[idx] = position[deck[idx]]

        return list(deck)


            
            

        

        