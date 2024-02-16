class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folders = []

        for dir in logs:
            if folders and dir == '../':
                folders.pop()

            elif dir not in '../':
                folders.append(dir)

        print(folders)
        return len(folders)