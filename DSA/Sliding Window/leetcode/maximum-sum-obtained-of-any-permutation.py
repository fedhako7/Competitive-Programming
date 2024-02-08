class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        all_requests = [0] * (len(nums) + 1)
        max_sum = 0

        for start, end in requests:
            all_requests[start] += 1
            all_requests[end + 1] -= 1

        all_requests.pop()
        for idx in range(1, len(all_requests)):
            all_requests[idx] += all_requests[idx - 1]

        all_requests.sort()
        nums.sort()
        
        print(nums)
        print(all_requests)
        for num, req in zip(nums, all_requests):
            max_sum += (num * req)

        return max_sum % (10 ** 9 + 7)
        