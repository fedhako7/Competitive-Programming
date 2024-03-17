class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        answer = [0] * len(queries)

        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for idx in range(1, len(nums)):
            prefix[idx] += (prefix[idx - 1] + nums[idx])

        print(prefix)
        for idx in range(len(queries)):
            index = 0
            while index < len(nums) and prefix[index] <= queries[idx]:
                index += 1

            answer[idx] = index


        return answer


