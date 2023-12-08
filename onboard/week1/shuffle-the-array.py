class Solution(object):
    def shuffle(self, nums, n):
        
        nums2 = [0] * len(nums)
        l = 0
        for i in range(len(nums)):
            if not i % 2:
                nums2[i] = nums[l]
            else:
                nums2[i] = nums[n + l]
                l +=1

        return nums2

        '''
        nums2, nums = nums[n+1:], nums[:n+1]
        nums3 = [''] * 2*n

        i1,i2 = 0, 0
        for i in range(n):
            if i % 2 == 0:
                nums3[i1+i2] = nums[i1]
                i1+=1
            else:
                nums3[i1+i2] = nums2[i2]
                i2+=1
        return nums'''