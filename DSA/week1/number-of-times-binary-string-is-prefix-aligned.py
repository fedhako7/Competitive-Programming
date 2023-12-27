class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        max_reach = float('-inf')

        for i in range(len(flips)):
            max_reach = max(max_reach, flips[i])
            if i + 1 == max_reach:
                count += 1

        return count
        