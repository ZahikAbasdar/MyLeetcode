from collections import Counter
from typing import List


class Solution:

    def largestOverlap(
        self, img1: List[List[int]], img2: List[List[int]]
    ) -> int:
        n = len(img1)

        # 1. Extract coordinates of all 1s
        ones1 = [
            (r, c) for r in range(n) for c in range(n) if img1[r][c] == 1
        ]
        ones2 = [
            (r, c) for r in range(n) for c in range(n) if img2[r][c] == 1
        ]

        # 2. Count occurrences of each shift vector (r1 - r2, c1 - c2)
        shift_counts = Counter()
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift_counts[(r1 - r2, c1 - c2)] += 1

        # 3. Return maximum overlap (or 0 if no 1s exist)
        return max(shift_counts.values()) if shift_counts else 0