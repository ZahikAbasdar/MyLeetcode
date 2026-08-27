from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        
        # Try finding the longest matching prefix target[:i]
        # and replacing target[i] with a strictly greater available character from s.
        for i in range(n - 1, -1, -1):
            # Calculate remaining character counts after matching target[:i]
            prefix_cnt = Counter(target[:i])
            
            # Verify target[:i] can be formed using available characters in s
            if any(prefix_cnt[ch] > cnt[ch] for ch in prefix_cnt):
                continue
            
            # Count of available letters left for index i and beyond
            avail = cnt - prefix_cnt
            
            # Try to place a character strictly greater than target[i] at position i
            for c in range(ord(target[i]) + 1, ord('z') + 1):
                char = chr(c)
                if avail[char] > 0:
                    # Found the latest valid branch! Construct the result string:
                    res = list(target[:i])
                    res.append(char)
                    avail[char] -= 1
                    
                    # Append remaining available characters in lexicographical order
                    for ch_code in range(ord('a'), ord('z') + 1):
                        ch_str = chr(ch_code)
                        res.append(ch_str * avail[ch_str])
                    
                    return "".join(res)
                    
        return ""