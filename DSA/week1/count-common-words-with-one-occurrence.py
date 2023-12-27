class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = 0 
        count1 = collections.Counter(words1)
        count2 = collections.Counter(words2)

        for string in count1:
            if count1[string] == 1 and string in count2 and count2[string] == 1:
                count += 1


        return count