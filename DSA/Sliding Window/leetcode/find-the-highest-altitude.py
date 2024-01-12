class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0

        sum_ = 0
        for high in gain:
            sum_ += high
            highest = max(highest, sum_)

        return highest