class Solution:
    def trap(self, height: List[int]) -> int:
        L = len(height)
        maxLeft = []
        maxRight = [0] * L

        maxL = 0

        for idx in range(L):
            maxLeft.append(maxL)
            maxL = max(maxL, height[idx])

        maxR = 0
        for idx in range(L -1, -1, -1):
            maxRight[idx] = maxR
            maxR = max(maxR, height[idx])


        trap = 0
        for idx in range(L):
            curr = min(maxRight[idx], maxLeft[idx]) - height[idx]
            if curr > 0:
                trap += curr


        return trap