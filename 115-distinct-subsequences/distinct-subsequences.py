class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # dp[j] stores the number of subsequences of s that equal t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: an empty string t is a subsequence of any prefix of s

        for char in s:
            # Iterate backwards to use values from the previous iteration
            for j in range(n, 0, -1):
                if char == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]