class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        prev = points[0]
        tot = 1
       
        for start, end in points:
            if start > prev[1]:
                tot += 1
                prev = [start, end]

            else:
                prev[1] = min(prev[1], end)

        return tot