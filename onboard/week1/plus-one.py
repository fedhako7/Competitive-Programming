class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for idx in range(len(digits) - 1, -1, -1):
            if digits[idx] != 9:
                digits[idx] += 1
                return digits
            digits[idx] = 0

        digits = [1] + [0] * len(digits)
        return digits
        