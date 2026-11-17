class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # Precompute divisors for each length from 1 to n
        divisors = [[] for _ in range(n + 1)]
        for length in range(1, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)
        
        # Helper to find changes needed to make s[i..j] a semi-palindrome
        def get_cost(i, j):
            length = j - i + 1
            min_changes = float('inf')
            
            for d in divisors[length]:
                current_changes = 0
                for start in range(d):
                    group_chars = []
                    idx = i + start
                    while idx <= j:
                        group_chars.append(s[idx])
                        idx += d
                    
                    left, right = 0, len(group_chars) - 1
                    while left < right:
                        if group_chars[left] != group_chars[right]:
                            current_changes += 1
                        left += 1
                        right -= 1
                min_changes = min(min_changes, current_changes)
                
            return min_changes

        # Precompute cost for all substrings s[i..j]
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                cost[i][j] = get_cost(i, j)

        # dp[i][p] -> min changes to partition prefix s[0..i-1] into p parts
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(p, n + 1):
                for j in range(p - 1, i):
                    if dp[j][p - 1] != float('inf'):
                        dp[i][p] = min(dp[i][p], dp[j][p - 1] + cost[j][i - 1])

        return dp[n][k]