class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums)):
            nums[i] = str(nums[i])

            def compare(str1, str2):
                if str1 + str2 > str2 + str1:
                    return -1
                else:
                    return 1

        strs = sorted(nums, key = cmp_to_key(compare))


        return str(int(''.join(strs)))


