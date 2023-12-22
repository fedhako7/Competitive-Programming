class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        candidates = [nums[0]] 

        for num in nums:
            if len(candidates) == 1:                    #[1,2,1,2,1,2,1,2,1,2]
                if num < candidates[0]:
                    candidates[0] = num
                elif num > candidates[0]:
                    candidates.append(num)
            else:
                if num < candidates[0]:
                    candidates[0] = num
                elif num < candidates[1] and num > candidates[0]:
                    candidates[1] = num
                elif num > candidates[1]:
                    return True
        
        return False