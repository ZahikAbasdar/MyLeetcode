from collections import deque

class Solution:
    def minimumObstacles(self, grid):
        m, n = len(grid), len(grid[0])

        # dist[i][j] = minimum obstacles removed to reach (i, j)
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        dq = deque([(0, 0)])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while dq:
            r, c = dq.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    cost = grid[nr][nc]
                    new_cost = dist[r][c] + cost

                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost

                        if cost == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))

        return dist[m - 1][n - 1]