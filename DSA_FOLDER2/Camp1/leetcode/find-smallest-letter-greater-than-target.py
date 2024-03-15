class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:


        low = -1
        high = len(letters)
        while low + 1 < high:
            mid = (low + high) // 2

            if letters[mid] > target:
                high = mid

            else:
                low = mid

        if high == len(letters):
            return letters[0]

        return letters[high]
        
        