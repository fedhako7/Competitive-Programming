class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p_holder = 1
        seeker = 1

        while seeker < len(nums):
            while (seeker < len(nums)) and (nums[seeker] == nums[seeker - 1]):
                seeker += 1

            if (p_holder < len(nums)) and (seeker < len(nums)):
                nums[p_holder] = nums[seeker]
                p_holder += 1
                seeker += 1


        return p_holder
        