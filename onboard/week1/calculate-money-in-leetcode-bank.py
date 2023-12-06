class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        fm = 1
        nd
        [mtwtfssmt]
        """
        first_mon = 0 
        next_day = first_mon
        total=0
        
        for i in range(1, n + 1):
            if i % 7 == 1:
                first_mon += 1
                next_day = first_mon
            else:
                next_day += 1
            total += next_day

        return total
                


            

        