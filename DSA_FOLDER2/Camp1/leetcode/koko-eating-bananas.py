class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canFinish(speed):
            speedHour = 0
            for pile in piles:
                speedHour += (pile // speed)
                if pile % speed:
                    speedHour += 1
                if speedHour > h:
                    return False

            return speedHour <= h

        

        #Fast will be the minimum of all possible value of k
        slow = 0
        fast = max(piles)
        while slow + 1 < fast:
            speed = (slow + fast) // 2
            if canFinish(speed):
                fast = speed
            else:
                slow = speed

        return fast
