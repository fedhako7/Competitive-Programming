class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for idx in range(len(nums) - 2):
            if idx > 0 and nums[idx - 1] == nums[idx]:
                continue

            left, right = idx + 1, len(nums) - 1
            while left < right:
                sum_ = nums[idx] + nums[left] + nums[right]
                if abs(closest - target) > abs(sum_ - target):
                    closest = sum_

                if sum_ == target:
                    return sum_

                elif sum_ < target:
                    left += 1

                else: 
                    right -= 1

        return closest
        