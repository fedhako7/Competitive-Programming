class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        penalities = [0] * (len(customers) + 1)
        penalities[-1] = 0
        count_p = 0

        
        for idx in range(len(customers) - 1, -1, -1):
            if customers[idx] == 'Y':
                count_p += 1 

            penalities[idx] = count_p

        
        count_p = 1 if customers[0] == 'N' else 0
        for idx in range(1, len(customers) + 1):
            penalities[idx] += count_p

            if idx < len(customers) and customers[idx] == 'N':
                count_p += 1


        min_p = min(penalities)
        for idx in range(len(penalities)):
            if penalities[idx] == min_p:
                return idx


        print(penalities)
        return -1