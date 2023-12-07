class Solution(object):
    def isAlienSorted(self, words, order):
        sorted_W = sorted(words, key=lambda word: [order.index(c) for c in word])
        return sorted_W == words