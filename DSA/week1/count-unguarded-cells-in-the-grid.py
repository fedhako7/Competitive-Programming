class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        count = 0
        grid = [['z'] * n for _ in range(m)]

        for row, col in guards:
            grid[row][col] = 'G'

        for row, col in walls:
            grid[row][col] = 'W'

        for guard in guards:
            row, col = guard

            # Check upward
            r = row - 1
            while r > -1 and grid[r][col] not in 'GW':
                if grid[r][col] != 'A':
                    grid[r][col] = 'A'
                    count += 1
                r -= 1
                
            # Check downward
            r = row + 1
            while r < m and grid[r][col] not in 'GW':
                if grid[r][col] != 'A':
                    grid[r][col] = 'A'
                    count += 1
                r += 1

            # Check to the left
            c = col - 1
            while c > -1 and grid[row][c] not in 'GW':
                if grid[row][c] != 'A':
                    grid[row][c] = 'A'
                    count += 1
                c -= 1

            # Check to the right
            c = col + 1
            while c < n and grid[row][c] not in 'GW':
                if grid[row][c] != 'A':
                    grid[row][c] = 'A'
                    count += 1
                c += 1

        unguarded_cell = (m * n) - (len(guards) + len(walls) + count)

        print('count', count, grid)
        return unguarded_cell