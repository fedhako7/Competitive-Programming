class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = 0
        count10 = 0

        for bill in bills:
            if bill == 5:
                count5 += 1
            
            elif bill == 10:
                if count5 > 0:
                    count5 -= 1
                    count10 += 1
                
                else:
                    return False

            else:
                if count5 > 0 and count10 > 0:
                    count5 -= 1
                    count10 -= 1

                elif count5 - 3 >= 0:
                    count5 -= 3

                else: 
                    return False

            
        return True