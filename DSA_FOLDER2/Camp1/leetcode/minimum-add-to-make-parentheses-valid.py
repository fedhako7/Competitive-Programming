class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        needed = 0
        open = 0
        close = 0

        for br in s:
            if br == '(':
                open += 1

            elif br == ')':
                if open:
                    open -= 1

                else:
                    needed += 1


        needed += open

        return needed