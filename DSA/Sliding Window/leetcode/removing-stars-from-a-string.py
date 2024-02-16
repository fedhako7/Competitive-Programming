class Solution:
    def removeStars(self, s: str) -> str:
        chars = []

        for char in s:
            if chars and char == '*':
                chars.pop()

            else:
                chars.append(char)

        
        return ''.join(chars)