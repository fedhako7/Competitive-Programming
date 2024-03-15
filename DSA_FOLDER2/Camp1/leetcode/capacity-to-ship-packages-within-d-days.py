class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def checkMinCapac(capacity):
            capacDays = 1
            currPackage = 0
            for weight in weights:

                currPackage += weight
                if currPackage > capacity:
                    capacDays += 1
                    currPackage = weight
                
                if capacDays > days:
                    return False

            return capacDays <= days
                    


        low = max(weights) - 1
        high = sum(weights)
        while low + 1 < high:
            capacity = (low + high) // 2

            if checkMinCapac(capacity):
                high = capacity

            else:
                low = capacity

        return high









