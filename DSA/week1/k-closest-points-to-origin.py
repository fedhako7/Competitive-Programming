class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def compare(point):
            return (point[0] ** 2) + (point[1] ** 2)

        
        points.sort(key = compare)

        return points[ :k]