class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count_num = collections.Counter(nums)
        
        for key in count_num:
            if count_num[key] % 2:
                return False

        return True