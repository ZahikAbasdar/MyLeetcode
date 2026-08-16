from functools import lru_cache

class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        # Base happiness & neighbor interactions table
        # 0: Empty, 1: Introvert, 2: Extrovert
        cost = [
            [0, 0, 0],
            [0, -60, -10],  # Introvert-Introvert (-30 - 30), Introvert-Extrovert (-30 + 20)
            [0, -10, 40]    # Extrovert-Introvert (+20 - 30), Extrovert-Extrovert (+20 + 20)
        ]
        
        @lru_cache(None)
        def dp(pos, intro, extro, last_n):
            if pos == m * n or (intro == 0 and extro == 0):
                return 0
            
            r, c = divmod(pos, n)
            res = 0
            
            # Option 0: Place nothing
            next_last_n = last_n[1:] + (0,)
            res = max(res, dp(pos + 1, intro, extro, next_last_n))
            
            # Option 1: Place Introvert
            if intro > 0:
                gain = 120
                if c > 0 and last_n[-1] != 0:  # Left neighbor
                    gain += cost[1][last_n[-1]]
                if last_n[0] != 0:             # Top neighbor
                    gain += cost[1][last_n[0]]
                
                next_last_n = last_n[1:] + (1,)
                res = max(res, gain + dp(pos + 1, intro - 1, extro, next_last_n))
                
            # Option 2: Place Extrovert
            if extro > 0:
                gain = 40
                if c > 0 and last_n[-1] != 0:  # Left neighbor
                    gain += cost[2][last_n[-1]]
                if last_n[0] != 0:             # Top neighbor
                    gain += cost[2][last_n[0]]
                
                next_last_n = last_n[1:] + (2,)
                res = max(res, gain + dp(pos + 1, intro, extro - 1, next_last_n))
                
            return res

        return dp(0, introvertsCount, extrovertsCount, (0,) * n)