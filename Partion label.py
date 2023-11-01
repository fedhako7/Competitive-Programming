class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_list = {c:i for i, c in enumerate(s)}
        size, max_idx, ans = 1, 0, []
        for i, c in enumerate(s):
            max_idx = max(max_idx, last_list[c])
            if i == max_idx:
                ans.append(size)
                size = 1
            else:
                size += 1

        return ans
