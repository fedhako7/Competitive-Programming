class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums[queries[0][1]] += queries[0][0]
        tot = [num for num in nums if not num % 2]
        answer = [0] * len(nums)
        answer[0] = sum(tot)

        for idx in range(len(queries)):
            if idx == 0:
                continue
            num, val = nums[queries[idx][1]], queries[idx][0] 
            if num % 2 and val % 2:
                answer[idx] = answer[idx - 1] + num + val
            elif not num % 2 and not val % 2:
                answer[idx] = answer[idx - 1] + val
            elif not num % 2 and val % 2:
                answer[idx] = answer[idx - 1] - num
            else:
                answer[idx] = answer[idx - 1]
            nums[queries[idx][1]] += queries[idx][0]

        return answer
           