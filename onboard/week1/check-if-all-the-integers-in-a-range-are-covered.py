class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        given_inter = set(range(left, right + 1))
        for r in ranges:
            curr_inter = set(range(r[0], r[1] + 1))
            given_inter.difference_update(curr_inter)

            if not given_inter:
                return True

        return False
        