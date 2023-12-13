class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        nums_idx = {nums[i]: i for i in range(len(nums))}
        

        for i in range(len(operations)):

            idx = nums_idx[operations[i][0]]
            nums[idx] = operations[i][1]
            nums_idx[nums[idx]] = idx
            nums_idx.pop(operations[i][0])
            
        return nums