class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        
        for idx in range(len(nums) - 2):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            left, right = idx + 1, len(nums) - 1

            while left < right:
                a, b, c = nums[left], nums[right], nums[idx]
                if a + b + c == 0:
                    triplets.append(sorted([a, b, c]))
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif a + b + c < 0:
                    left += 1

                else:
                    right -= 1

        
        return triplets