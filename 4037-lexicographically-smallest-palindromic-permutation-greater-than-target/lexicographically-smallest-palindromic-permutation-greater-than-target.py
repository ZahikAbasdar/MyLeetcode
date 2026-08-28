from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        # Check if a valid palindromic permutation can be formed
        odd_chars = [char for char, count in counts.items() if count % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        
        # Build frequency map for the first half
        half_counts = {char: count // 2 for char, count in counts.items()}
        half_len = n // 2
        
        # Helper to construct the smallest remaining string from counts
        def get_smallest(avail_counts):
            res = []
            for ch in sorted(avail_counts.keys()):
                res.append(ch * avail_counts[ch])
            return "".join(res)
        
        # Helper to assemble the full palindrome given first half prefix
        def build_palindrome(first_half):
            if n % 2 == 1:
                return first_half + mid_char + first_half[::-1]
            return first_half + first_half[::-1]

        # Try to find the common prefix matching target[0..i-1],
        # then set target[i] to a larger character ch > target[i].
        # Iterate i from half_len down to 0 to find the longest valid matching prefix.
        
        best_res = None
        
        # Case 1: First half matches target[:half_len] completely
        prefix = []
        curr_counts = half_counts.copy()
        can_match_prefix = True
        
        for i in range(half_len):
            ch = target[i]
            if curr_counts.get(ch, 0) > 0:
                prefix.append(ch)
                curr_counts[ch] -= 1
            else:
                can_match_prefix = False
                break
                
        if can_match_prefix:
            first_half = "".join(prefix)
            candidate = build_palindrome(first_half)
            if candidate > target:
                best_res = candidate

        # Case 2: Diverge at position i (0 <= i < half_len), picking a larger char at position i
        for i in range(half_len - 1, -1, -1):
            # Reconstruct prefix up to index i-1
            curr_counts = half_counts.copy()
            possible = True
            for j in range(i):
                ch = target[j]
                if curr_counts.get(ch, 0) > 0:
                    curr_counts[ch] -= 1
                else:
                    possible = False
                    break
            
            if not possible:
                continue
                
            prefix_str = target[:i]
            target_char = target[i]
            
            # Try available characters larger than target[i]
            for larger_char in sorted(curr_counts.keys()):
                if larger_char > target_char and curr_counts[larger_char] > 0:
                    temp_counts = curr_counts.copy()
                    temp_counts[larger_char] -= 1
                    
                    first_half = prefix_str + larger_char + get_smallest(temp_counts)
                    candidate = build_palindrome(first_half)
                    
                    if candidate > target:
                        if best_res is None or candidate < best_res:
                            best_res = candidate
                    # Since we pick the smallest larger_char first, breaking here gives 
                    # the smallest valid candidate for this mismatch index i.
                    break
        
        return best_res if best_res is not None else ""