class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        inter = []
        for left, right in firstList:
            for left2, right2 in secondList:
                if (not left2 > right) and (not left > right2):
                    intr = [max(left, left2), min(right, right2)]
                    inter.append(intr)

        return inter