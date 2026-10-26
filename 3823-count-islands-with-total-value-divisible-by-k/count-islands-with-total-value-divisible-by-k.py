class Solution:

  def countIslands(self, grid: List[List[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    count = 0

    def dfs(r, c):
      # Stack-based or recursive DFS to traverse the connected land cells (> 0)
      stack = [(r, c)]
      visited[r][c] = True
      total_sum = 0

      while stack:
        curr_r, curr_c = stack.pop()
        total_sum += grid[curr_r][curr_c]

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          nr, nc = curr_r + dr, curr_c + dc
          if (
              0 <= nr < m
              and 0 <= nc < n
              and not visited[nr][nc]
              and grid[nr][nc] > 0
          ):
            visited[nr][nc] = True
            stack.append((nr, nc))

      return total_sum

    for i in range(m):
      for j in range(n):
        if grid[i][j] > 0 and not visited[i][j]:
          island_sum = dfs(i, j)
          if island_sum % k == 0:
            count += 1

    return count