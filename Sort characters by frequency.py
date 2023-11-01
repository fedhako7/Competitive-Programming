from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = '' # Initialize empty string
        freq = Counter(s) 
        sorted_freq = sorted(freq, key = lambda a : freq[a], reverse = True)

        for c in sorted_freq:
            ans += c * freq[c]

        return ans
