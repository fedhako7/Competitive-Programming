class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        reminders = collections.defaultdict(int)
        reminders[0] = 1
        dividend = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num
            reminder = curr_sum % k
            dividend += reminders[reminder]
            reminders[reminder] += 1

        return dividend
