from collections import Counter

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        total_k = k1 + k2
        
        # Step 1: Calculate absolute differences and their frequencies
        diff_counts = Counter(abs(n1 - n2) for n1, n2 in zip(nums1, nums2))
        max_diff = max(diff_counts.keys()) if diff_counts else 0
        
        # Step 2: Greedily reduce the largest differences
        curr_diff = max_diff
        while curr_diff > 0 and total_k > 0:
            count = diff_counts[curr_diff]
            if count <= total_k:
                # We can reduce all elements at curr_diff down to curr_diff - 1
                total_k -= count
                diff_counts[curr_diff] = 0
                diff_counts[curr_diff - 1] += count
            else:
                # We can only reduce a portion of elements at curr_diff
                diff_counts[curr_diff] -= total_k
                diff_counts[curr_diff - 1] += total_k
                total_k = 0
                break
            curr_diff -= 1
            
        # Step 3: Calculate the final sum of squared differences
        ans = 0
        for diff, count in diff_counts.items():
            if diff > 0 and count > 0:
                ans += (diff ** 2) * count
                
        return ans