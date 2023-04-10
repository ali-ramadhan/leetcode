# Return 1 if we visited a new island, otherwise 0.
def new_island(i, j, land, visited):
    if visited[i][j] == 1:
        return False
    
    visited[i][j] = 1

    for neighbor in land[(i, j)]:
        ii, jj = neighbor
        new_island(ii, jj, land, visited)
    
    return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Create graph of connected land points.
        land = {}
        for i in range(m):
            for j in range(n):
                if int(grid[i][j]) == 1:
                    land[(i, j)] = []
                    if i-1 >= 0 and int(grid[i-1][j]) == 1:
                        land[(i, j)].append((i-1, j))
                    if i+1 < m and int(grid[i+1][j]) == 1:
                        land[(i, j)].append((i+1, j))
                    if j-1 >= 0 and int(grid[i][j-1]) == 1:
                        land[(i, j)].append((i, j-1))
                    if j+1 < n and int(grid[i][j+1]) == 1:
                        land[(i, j)].append((i, j+1))

        # Perform a depth-first search on the land graph, starting from each land point.
        visited = [[0] * n for _ in range(m)]
        islands = 0
        for point in land:
            i, j = point
            if new_island(i, j, land, visited):
                islands += 1
        
        return islands
