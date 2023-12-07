class Solution(object):
    def numberOfMatches(self, n):
        """
        
        
        """
        matches = 0
        while n >= 2:
            if n % 2 == 0:
                matches += n / 2
                n = (n / 2)
            else:
                matches += (n - 1) / 2
                n = (n + 1) / 2
        
        return matches
        