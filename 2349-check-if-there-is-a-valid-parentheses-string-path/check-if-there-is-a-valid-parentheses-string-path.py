class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Pruning 1: A valid path length (m + n - 1) must be even
        if (m + n - 1) % 2 != 0:
            return False
            
        # Pruning 2: The path must start with an open bracket and end with a closed bracket
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
            
        from functools import cache
        
        @cache
        def dfs(r, c, balance):
            # Update balance based on the current cell
            balance += 1 if grid[r][c] == '(' else -1
            
            # A valid parentheses string cannot have more closing brackets than opening ones at any point
            if balance < 0:
                return False
                
            # If we reached the end, the brackets must be perfectly balanced
            if r == m - 1 and c == n - 1:
                return balance == 0
                
            # Explore moving down (r+1) and moving right (c+1)
            # If any of these paths return True, we found a valid path
            if r + 1 < m and dfs(r + 1, c, balance):
                return True
            if c + 1 < n and dfs(r, c + 1, balance):
                return True
                
            return False
            
        # Start at top-left with an initial balance of 0
        return dfs(0, 0, 0)