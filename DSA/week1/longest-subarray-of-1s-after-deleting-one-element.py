class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count_ones = 0
        curr_ones, rule = 0, 0

        del_found = False
        left, right = 0, 0
        while right < len(nums):
            if nums[right] == 1:
                curr_ones += 1
             
            elif nums[right] != 1:
                rule += 1
                del_found = True

            while rule > 1:
                if nums[left] == 1:
                    curr_ones -= 1

                elif nums[left] != 1:
                    rule -= 1

                left += 1
            
            count_ones = max(count_ones, curr_ones)
            
            right += 1

        count_ones = count_ones if del_found else count_ones - 1
        return count_ones