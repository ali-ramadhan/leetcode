class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        distance = [[0 for j in range(n)] for i in range(m)]

        # Add all zero-cells to q.
        q = deque([])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    distance[i][j] = -1  # Yet to be processed.

        dir1 = [0, 1, 0, -1]
        dir2 = [1, 0, -1, 0]

        while q:
            r, c = q.popleft()
            for d1, d2 in zip(dir1, dir2):
                nr = r + d1
                nc = c + d2

                # If we're out of bounds or we have already visited (nr, nc) then continue.
                if nr < 0 or nr == m or nc < 0 or nc == n or distance[nr][nc] != -1:
                    continue

                # Otherwise we're 1 away from cell (r, c).
                distance[nr][nc] = distance[r][c] + 1

                # Let's visit this cell for its nearest neighbors later.
                q.append((nr, nc))
        
        return distance
