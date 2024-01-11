class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def compar(num1, num2):
            if num1 < num2:
                return -1

            elif num2 < num1:
                return 1
            else:
                return 0

        
        nums.sort(key = cmp_to_key(compar))

        return nums