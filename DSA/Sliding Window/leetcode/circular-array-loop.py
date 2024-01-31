class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        seen = set()

        for idx in range(len(nums)):
            if idx not in seen:
                curr_cycle = set()

                while True:
                    if idx in curr_cycle:
                        return True

                    seen.add(idx)
                    curr_cycle.add(idx)
                    prev, idx = idx, (idx + nums[idx]) % len(nums)
                    
                    if prev == idx or (nums[prev] * nums[idx]) < 0:
                        break

        
        return False

