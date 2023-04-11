EMPTY = 0
FRESH = 1
ROTTEN = 2

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        minute = 0
        while True:
            new_rottens = set()
            for i in range(m):
                for j in range(n):
                    # We only need to evolve cells neighboring a rotten cell.
                    if grid[i][j] != ROTTEN:
                        continue
                    if i-1 >= 0 and grid[i-1][j] == FRESH:
                        new_rottens.add((i-1, j))
                    if i+1 < m and grid[i+1][j] == FRESH:
                        new_rottens.add((i+1, j))
                    if j-1 >= 0 and grid[i][j-1] == FRESH:
                        new_rottens.add((i, j-1))
                    if j+1 < n and grid[i][j+1] == FRESH:
                        new_rottens.add((i, j+1))
            
            if len(new_rottens) == 0:
                # No new rotten oranges means we're done.
                break
            else:
                for i, j in new_rottens:
                    grid[i][j] = ROTTEN
            minute += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == FRESH:
                    return -1

        return minute
