class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [0] * len(nums)
        products[0] = 1
        product = 1

        for idx in range(1, len(nums)):
            product *= nums[idx - 1]
            products[idx] = product

        product = 1
        for idx in range(len(nums) - 2, -1, -1):
            product *= nums[idx + 1]
            products[idx] *= product

        return products