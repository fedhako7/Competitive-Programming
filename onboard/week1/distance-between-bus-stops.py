class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        if start > destination:
            start, destination = destination, start

        clockwise = sum(distance[start: destination])
        anticlk = sum(distance) - clockwise

        return min(clockwise, anticlk)