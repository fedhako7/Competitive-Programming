class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        minRemove = 0

        prev = intervals[0]
        for idx in range(1, len(intervals)):
            if intervals[idx][0] < prev[1]:
                minRemove += 1
                prev[1] = min(intervals[idx][1], prev[1])

            else:
                prev[1] = intervals[idx][1]


        return minRemove