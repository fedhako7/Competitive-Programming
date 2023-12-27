class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num_dict = defaultdict(list)
        seen = []
        

        for num in nums:
            if num not in seen:
                seen.append(num)
                freq = nums.count(num)
                num_dict[freq].extend([num] * freq)

        sorted_key = sorted(num_dict)
        nums = []
        for key in sorted_key:
            sort_num = sorted(num_dict[key], reverse = True)
            nums.extend(sort_num)


        return nums