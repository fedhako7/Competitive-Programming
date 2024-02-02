class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        uniques = set(nums)
        sub_elements = collections.defaultdict(int)
        sub_array = 0

        left = 0
        for right in range(len(nums)):
            sub_elements[nums[right]] += 1

            if len(sub_elements) == len(uniques):
                sub_array +=  len(nums) - right

            while left <= right and len(sub_elements) == len(uniques):
                sub_elements[nums[left]] -= 1

                if sub_elements[nums[left]] == 0:
                    del sub_elements[nums[left]]

                else:
                    sub_array += len(nums) - right

                left += 1


        return sub_array