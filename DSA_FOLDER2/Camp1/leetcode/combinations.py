class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        

        def helper(choice, path):
            
            if len(path) == k:
                combs.append(path[:])
                return

            for idx in range(choice, n + 1):
                path.append(idx)
                helper(idx + 1, path)
                path.pop()


        helper(1, [])
        return combs