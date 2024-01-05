class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        def compar(even, odd):
            if even % 2 == 0 and odd % 2 == 1:
                return -1
            elif even % 2 == 1 and odd % 2 == 0: 
                return 1
            else: # Return 0 if both numbers are even or odd
                return 0

        nums.sort(key = cmp_to_key(compar))
        return nums