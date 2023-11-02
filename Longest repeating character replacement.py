from collections import Counter

class Solution:
    def characterReplacement(self, s, k):
        maxFreq = 0
        result=0
        counter = Counter()
        
        slow = 0
        fast = 0
        N = len(s)
        while fast<N:
            counter[s[fast]]+=1
            maxFreq = max(maxFreq, counter[s[fast]])
            
            if (fast-slow+1)-maxFreq > k:
                counter[s[slow]]-=1
                slow+=1
            result = max(result, (fast-slow+1))    
            fast+=1
            
        return result
