from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        
        # Segment tree arrays
        # tree_tot[i] stores the total product modulo k for the node's range
        # tree_cnt[i][c] stores the count of prefixes in the node's range with product modulo k == c
        tree_tot = [0] * (2 * n)
        tree_cnt = [[0] * k for _ in range(2 * n)]
        
        # 1. Initialize leaves
        for i in range(n):
            v = nums[i] % k
            tree_tot[n + i] = v
            tree_cnt[n + i][v] = 1
            
        # 2. Build the tree iteratively (bottom-up)
        for i in range(n - 1, 0, -1):
            left = 2 * i
            right = 2 * i + 1
            tree_tot[i] = (tree_tot[left] * tree_tot[right]) % k
            
            # Copy left child's prefix counts
            for c in range(k):
                tree_cnt[i][c] = tree_cnt[left][c]
                
            # Add right child's prefix counts offset by left child's total product
            lt = tree_tot[left]
            for c in range(k):
                if tree_cnt[right][c] > 0:
                    tree_cnt[i][(lt * c) % k] += tree_cnt[right][c]
                    
        ans = []
        
        for idx, val, start, x in queries:
            # --- Update Point ---
            pos = n + idx
            v = val % k
            tree_tot[pos] = v
            for c in range(k):
                tree_cnt[pos][c] = 0
            tree_cnt[pos][v] = 1
            
            pos //= 2
            while pos > 0:
                left = 2 * pos
                right = 2 * pos + 1
                tree_tot[pos] = (tree_tot[left] * tree_tot[right]) % k
                
                for c in range(k):
                    tree_cnt[pos][c] = tree_cnt[left][c]
                    
                lt = tree_tot[left]
                for c in range(k):
                    if tree_cnt[right][c] > 0:
                        tree_cnt[pos][(lt * c) % k] += tree_cnt[right][c]
                pos //= 2
            
            # --- Range Query ---
            l = n + start
            r = n + n - 1
            left_nodes = []
            right_nodes = []
            
            # Identify O(log N) segments that cover the range [start, n-1]
            while l <= r:
                if l % 2 == 1:
                    left_nodes.append(l)
                    l += 1
                if r % 2 == 0:
                    right_nodes.append(r)
                    r -= 1
                l //= 2
                r //= 2
                
            curr_tot = 1 % k
            curr_cnt = [0] * k
            
            # Merge identified segments strictly from left to right
            for node in left_nodes + right_nodes[::-1]:
                nxt_tot = (curr_tot * tree_tot[node]) % k
                nxt_cnt = list(curr_cnt)
                
                for c in range(k):
                    if tree_cnt[node][c] > 0:
                        nxt_cnt[(curr_tot * c) % k] += tree_cnt[node][c]
                        
                curr_tot = nxt_tot
                curr_cnt = nxt_cnt
                
            ans.append(curr_cnt[x])
            
        return ans