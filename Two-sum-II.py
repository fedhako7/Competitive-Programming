class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
 
        l, r = 0, len(numbers) - 1
        while l < r:
            twoSum = numbers[l] + numbers[r]
            if twoSum == target:
                return [l + 1, r + 1]
            elif twoSum > target:
                r -= 1
                if r < len(numbers) - 1 and numbers[r] == numbers[r + 1]:
                    continue
            else:
                l += 1
                if l > 0 and numbers[l - 1] == numbers[l]:
                    continue

        return []
