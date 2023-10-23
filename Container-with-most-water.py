class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        l, r = 0, len(height) - 1
        while l < r:
            top = height[l] if height[l] < height[r] else height[r]

            if (r - l) * top > maxArea:
                maxArea = (r - l) * top

            if height[l] < height[r]:
                l += 1
                if l > 0 and height[l] <= height[l - 1]:
                    continue
            else:
                r -= 1
                if r < len(height) - 1 and height[r] <= height[r + 1]:
                    continue
        return maxArea
