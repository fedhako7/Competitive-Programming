class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        content = 0
        g.sort()
        s.sort()

        point_g, point_s = 0, 0
        while (point_g < len(g)) and (point_s < len(s)):
            if g[point_g] <= s[point_s]:
                content += 1 
                point_g += 1 
                point_s += 1

            else:
                point_s += 1


        return content
        