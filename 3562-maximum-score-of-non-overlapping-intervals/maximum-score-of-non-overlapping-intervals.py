from bisect import bisect_right
from functools import lru_cache
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        # Store original indices: [l, r, weight, original_index]
        sorted_intervals = sorted(
            [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        )
        
        # Extract start times for binary search
        starts = [interval[0] for interval in sorted_intervals]
        
        @lru_cache(None)
        def solve(i: int, k: int):
            if i == n or k == 0:
                return (0, ())
            
            # Option 1: Skip the current interval
            res_skip = solve(i + 1, k)
            
            # Option 2: Take the current interval
            l, r, w, idx = sorted_intervals[i]
            # Find first interval starting at or after r + 1
            next_idx = bisect_right(starts, r)
            
            next_score, next_path = solve(next_idx, k - 1)
            
            # Sort the indices sequence to maintain lexicographical order requirement
            curr_path = tuple(sorted(next_path + (idx,)))
            res_take = (w + next_score, curr_path)
            
            # Compare (-score, path) to maximize score first, 
            # and break ties with lexicographically smaller index tuples
            if (-res_take[0], res_take[1]) < (-res_skip[0], res_skip[1]):
                return res_take
            else:
                return res_skip
        
        best_score, best_path = solve(0, 4)
        return list(best_path)