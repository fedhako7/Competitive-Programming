class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:



        def isExist(idx, half):
            targetArr = sorted(arr[ :idx] + arr[idx + 1: ])
            low = -1
            high = len(targetArr) - 1


            while low + 1 < high:
                mid = (low + high) // 2
                if targetArr[mid] < half:
                    low = mid
                elif targetArr[mid] == half:
                    return True
                else: 
                    high = mid


            return targetArr[high] == half 


       

        for idx, num in enumerate(arr):
            if num % 2 == 0:
                half = num // 2
                if isExist(idx, half):
                    return True

        return False


