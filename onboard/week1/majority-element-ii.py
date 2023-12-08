class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        stack = []
        appear = 1
        for idx in range(1, len(nums)):         

            if appear > len(nums) // 3:          
                stack.append(nums[idx - 1])
                appear = 1

            if nums[idx] == nums[idx - 1]:
                appear += 1
            else:
                appear = 1
        
        if appear > len(nums) // 3:          
            stack.append(nums[-1])

        return list(set(stack))