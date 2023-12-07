class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort(reverse = True)
        perim = 0
        for i in  range(len(nums) - 2):
            l, r = i + 1, i + 2
            if nums[i] < nums[l] + nums[r]:
                return nums[i] + nums[l] + nums[r]
        
        return 0

                
 

        