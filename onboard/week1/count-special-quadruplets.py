class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
       
        for a in range(len(nums) - 3):                     
            for b in range(a + 1, len(nums) - 2):
                for c in range(b + 1, len(nums) - 1):
                    for d in range(c + 1, len(nums)):
                        if (nums[a] + nums[b] + nums[c]) == nums[d]:
                            count += 1

        return count