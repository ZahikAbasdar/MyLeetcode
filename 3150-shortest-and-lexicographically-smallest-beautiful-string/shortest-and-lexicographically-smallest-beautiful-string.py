class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # If total number of '1's in s is less than k, no valid substring exists
        if s.count('1') < k:
            return ""
        
        # Collect 0-based indices of all '1's in the string
        ones = [i for i, ch in enumerate(s) if ch == '1']
        
        min_len = float('inf')
        ans = ""
        
        # Every beautiful substring starts at a '1' and ends at a '1' with k ones in total
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            sub = s[start : end + 1]
            
            # Update answer if substring is shorter or lexicographically smaller
            if len(sub) < min_len:
                min_len = len(sub)
                ans = sub
            elif len(sub) == min_len:
                ans = min(ans, sub)
                
        return ans