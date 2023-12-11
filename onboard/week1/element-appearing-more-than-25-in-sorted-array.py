class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        found = 1
        for i in range(len(arr)):
            if arr[i] == arr[i - 1]:
                found += 1
            else:
                found = 1
            if found / len(arr) > 1 / 4:
                return arr[i]
        