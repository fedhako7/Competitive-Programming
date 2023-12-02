class Solution(object):
    def mergeAlternately(self, word1, word2):
        idx1, idx2 = 0, 0
        flag, minLen = True, min(len(word1), len(word2))
        answer = ''
        for i in range(minLen * 2):
            if flag:
                answer = answer + word1[idx1]
                idx1 +=1
                flag = False
            else:
                answer = answer + word2[idx2]
                idx2 +=1
                flag = True
            
        return answer + word1[minLen : ] + word2[minLen : ]