class Solution:
    def reverseWords(self, s: str) -> str:
        s_lists = s.split()
        s_lists = s_lists[::-1]
        
        return ' '.join(s_lists)