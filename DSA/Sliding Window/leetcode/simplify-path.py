class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        canonical = []

        for dir in paths:
            if dir == '..':
                if canonical:
                    canonical.pop()

            elif dir != '' and dir != '.':
                canonical.append(dir)


        return '/' + '/'.join(canonical)