from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        

        idx_dict = defaultdict(list)
        arr = [0] * len(nums)

        for i in range(len(nums)):
            idx_dict[nums[i]].append(i)
        
        
        for indices in idx_dict.values():
            if len(indices) > 1:
                prefix = [0] * len(indices)
                postfix = [0] * len(indices)

                for idx in range(1, len(indices)):
                    prefix[idx] = prefix[idx - 1] + indices[idx - 1]

                for idx in range(len(indices) - 2, -1, -1):
                    postfix[idx] = postfix[idx + 1] + indices[idx + 1]


                for idx in range(len(indices)):
                    abs_diff = (indices[idx] * idx) - prefix[idx] # Left part
                    abs_diff += postfix[idx] - (indices[idx] * (len(indices) - idx - 1))
                    arr[indices[idx]] = abs_diff


        return arr
