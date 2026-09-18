class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # 1. Record the first and last occurrence of each character
        first = {}
        last = {}
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i

        intervals = []
        
        # 2. Find all valid intervals
        for char in set(s):
            L = first[char]
            R = last[char]
            i = L
            is_valid = True
            
            # Expand the window to include all occurrences of characters inside it
            while i <= R:
                # If a character inside the current window started before our starting 
                # point L, we cannot form a valid independent substring starting at L.
                if first[s[i]] < L:
                    is_valid = False
                    break
                # Extend the right boundary to ensure all occurrences are captured
                R = max(R, last[s[i]])
                i += 1
            
            if is_valid:
                intervals.append((L, R))
                
        # 3. Greedily pick intervals
        # Sort by right endpoint ascending (to leave maximum room for subsequent substrings)
        # In case of a tie, sort by left endpoint descending (to prioritize the shorter substring)
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        res = []
        prev_end = -1
        
        for L, R in intervals:
            # If the current interval doesn't overlap with the previously selected one
            if L > prev_end:
                res.append(s[L:R+1])
                prev_end = R
                
        return res