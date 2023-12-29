class Solution:
    def sortSentence(self, s: str) -> str:
        words = {}
        word = ''
        for idx in range(len(s)):
            if s[idx].isdigit():
                words[int(s[idx])] = word
                word = ''

            elif s[idx] != ' ':
                word = word + s[idx]

        words = dict(sorted(words.items()))

        return ' '.join(words.values())