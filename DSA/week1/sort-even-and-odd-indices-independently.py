class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odds = [nums[o] for o in range(len(nums)) if o % 2]
        evens = [nums[e] for e in range(len(nums)) if not e % 2]

        odds.sort(reverse = True)
        evens.sort()
        
        e_idx, o_idx = 0, 0
        for idx in range(len(nums)):
            if idx % 2 == 0:
                nums[idx] = evens[e_idx]
                e_idx += 1

            else:
                nums[idx] = odds[o_idx]
                o_idx += 1

        return nums