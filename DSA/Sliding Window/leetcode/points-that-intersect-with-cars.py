class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        points = [0] * 101
        
        for start, end in nums:
            start -= 1
            end -= 1
            points[start] += 1
            points[end + 1] -= 1


        for idx in range(1, 100):
            points[idx] += points[idx - 1]

        point = 0
        for idx in range(100):
            if points[idx]:
                point += 1


        return point