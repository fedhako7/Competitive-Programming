class Solution(object):
    def addSpaces(self, s, spaces):
        '''
        #Declare stack strings[] & append the first string from s[0:sp[0]]
        # Iterate from 1 to spaces len and slice  s[spaces[idx - 1:idx]]
        #Append them in stack strings[] 
        #return ' ' joined strings out of loop.
        '''
        strings = []
        strings.append(s[0:spaces[0]]) 

        for idx in range(1, len(spaces)):           
            strings.append(s[spaces[idx - 1] : spaces[idx]])

        strings.append(s[spaces[-1]:])              

        return ' '.join(strings)