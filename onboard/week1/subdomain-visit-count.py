class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_freq = {}
        splited = []

        for domains in cpdomains:
            right = len(domains) - 1
            idx = domains.index(' ')
            view = int(domains[ : idx])

            while right >= idx:
                if domains[right] in '. ':
                    visit_freq[domains[right + 1 : ]] = view + visit_freq.get(domains[right + 1 : ], 0)

                right -= 1

        splited = []
        for key, val in visit_freq.items():
            splited.append(str(val) + ' ' + str(key))
        
        return splited



                
            
                
            



        
        
        