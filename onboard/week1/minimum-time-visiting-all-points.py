class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        diag, hor, tm = 0, 0, 0

        for i in range(1, len(points)):
            diag = min(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1]))
            hor = max(abs((points[i][0] - points[i - 1][0])), abs(points[i][1] - (points[i - 1][1]))) - diag

            tm += diag
            tm += hor

        return tm