class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        length = 0
        k_part = num_str[ :k]

        if int(k_part) != 0 and num % int(k_part) == 0:
            length += 1

        for idx in range(k, len(num_str)):
            k_part = num_str[idx - k + 1 : idx + 1]
            if int(k_part) != 0 and num % int(k_part) == 0:
                length += 1

        return length

        