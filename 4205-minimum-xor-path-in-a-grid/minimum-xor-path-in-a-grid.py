class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[i][j] will store a set of all possible XOR values to reach cell (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        dp[0][0].add(grid[0][0])
        
        for i in range(m):
            for j in range(n):
                for val in dp[i][j]:
                    # Move right
                    if j + 1 < n:
                        dp[i][j + 1].add(val ^ grid[i][j + 1])
                    # Move down
                    if i + 1 < m:
                        dp[i + 1][j].add(val ^ grid[i + 1][j])
                        
        return min(dp[m - 1][n - 1])