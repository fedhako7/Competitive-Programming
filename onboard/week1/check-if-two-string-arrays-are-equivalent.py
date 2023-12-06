class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        check_equality = ''.join(word1) == ''.join(word2)
        return check_equality