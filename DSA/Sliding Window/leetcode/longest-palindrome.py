class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = defaultdict(int)

        for char in s:
            freq[char] += 1

        length = 0
        odd = 0

        freq = dict(freq)
        for char in freq.keys():
            if not freq[char]  % 2:
                length += freq[char]

            else:
                length += freq[char] - 1

            if freq[char] % 2:
                odd = 1    

        return length + odd