class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        L = len(cookies)
        dist = [0 for i in range(k)]
        unfair = float('inf')


        def backT(idx, dist):
            if idx == L:
                nonlocal unfair
                currDis = max(dist)
                unfair = min(unfair, currDis)
                return

            for i in range(k):
                dist[i] += cookies[idx]
                backT(idx + 1, dist)
                dist[i] -= cookies[idx]
                if idx == 0:
                    break

        

        backT(0, dist)

        return unfair

        