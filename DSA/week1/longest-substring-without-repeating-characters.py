class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        count_s = defaultdict(int)

        l = 0
        for i in range(len(s)):
            count_s[s[i]] += 1

            while count_s[s[i]] == 2:
                count_s[s[l]] -= 1
                l += 1
                
            curr_count = i - l + 1
            length = max(length, curr_count)

        return length