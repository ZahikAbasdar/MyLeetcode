import math

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # Calculate combinations C(n + k - 1, 2k)
        result = math.comb(n + k - 1, 2 * k)
        
        return result % MOD