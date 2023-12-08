class Solution(object):
    def pivotArray(self, nums, pivot):
        
        greats, smalls, equal = [], [], 0
        for idx in range(len(nums)):
            if nums[idx] > pivot:
                greats.append(nums[idx])
            elif nums[idx] < pivot:
                smalls.append(nums[idx])
            else:
                equal += 1
        equal = [pivot] * equal 
        smalls.extend(equal)
        smalls.extend(greats)



        return smalls