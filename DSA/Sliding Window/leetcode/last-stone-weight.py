class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 2:
            stones.sort()
            new_stone = stones.pop() - stones.pop()
            if new_stone:
                stones.append(new_stone)

        
        if len(stones) == 1:
            return stones[0]

        elif len(stones) == 2:
            return abs(stones.pop() - stones.pop())

        return 0