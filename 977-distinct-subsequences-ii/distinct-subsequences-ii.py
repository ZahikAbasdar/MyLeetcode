class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        # dp stores the total number of distinct subsequences (including empty string)
        dp = 1
        # last[c] stores how much dp increased when char c was previously appended
        last = {}

        for char in s:
            # New subsequences formed by appending 'char' equals current dp
            new_added = dp
            
            # dp doubles, but we subtract previously generated duplicates for 'char'
            dp = (dp * 2 - last.get(char, 0)) % MOD
            
            # Store the number of new subsequences added by this character
            last[char] = new_added

        # Subtract 1 to exclude the empty subsequence
        return (dp - 1) % MOD