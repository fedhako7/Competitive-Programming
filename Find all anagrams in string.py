from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        targetHM = Counter(p)
        sw = len(p)
        result = []
        i = 0
        j = i+sw-1
        tempHM = Counter(s[i:j])
        while i<(len(s)-sw+1):
            tempHM[s[j]]+=1
            match = True
            for k,v in targetHM.items():
                if k not in tempHM or tempHM[k]!=v:
                    match=False
                    break
            if match:
                result.append(i)
            tempHM[s[i]]-=1
            i+=1
            j+=1
        
        return result
