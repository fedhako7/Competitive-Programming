class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        count_jewel = 0
        
        for stone in stones:
            if stone in jewels:
                count_jewel += 1

        return count_jewel