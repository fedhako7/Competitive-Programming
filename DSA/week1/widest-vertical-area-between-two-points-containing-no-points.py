class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        widest = float('-inf')
        points.sort(key = lambda point: point[0])

        for idx in range(1, len(points)):
            prev = points[idx - 1]
            curr = points[idx]
            widest = max(widest, curr[0] - prev[0])

        return widest




