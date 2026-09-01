import math
from typing import List


class Solution:

    def maxActiveSectionsAfterTrade(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:
        n = len(s)

        # 1. Total active sections globally
        activeCount = sum(1 for ch in s if ch == "1")

        # 2. Identify zero-blocks (start and end indices)
        blockStart = []
        blockEnd = []
        i = 0
        while i < n:
            if s[i] == "0":
                start = i
                while i < n and s[i] == "0":
                    i += 1
                blockStart.append(start)
                blockEnd.append(i - 1)
            else:
                i += 1

        m = len(blockStart)

        # Base case: if fewer than 2 zero blocks exist, no trade creates extra active sections
        if m < 2:
            return [activeCount] * len(queries)

        # 3. Block sizes and adjacent pair sums
        blockSize = [blockEnd[k] - blockStart[k] + 1 for k in range(m)]

        N = m - 1
        pairSum = [blockSize[k] + blockSize[k + 1] for k in range(N)]

        # 4. Build Segment Tree over pairSum array
        st = [0] * (4 * N)

        def build(i: int, l: int, r: int):
            if l == r:
                st[i] = pairSum[l]
                return
            mid = l + (r - l) // 2
            build(2 * i + 1, l, mid)
            build(2 * i + 2, mid + 1, r)
            st[i] = max(st[2 * i + 1], st[2 * i + 2])

        build(0, 0, N - 1)

        def rmq(start: int, end: int, i: int, l: int, r: int) -> int:
            if l > end or r < start:
                return -float("inf")
            if l >= start and r <= end:
                return st[i]
            mid = l + (r - l) // 2
            return max(
                rmq(start, end, 2 * i + 1, l, mid),
                rmq(start, end, 2 * i + 2, mid + 1, r),
            )

        # Binary search helper functions
        def lowerBound(arr: List[int], key: int) -> int:
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if arr[mid] < key:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def upperBound(arr: List[int], key: int) -> int:
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if arr[mid] <= key:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        # 5. Process range queries
        result = []
        for l, r in queries:
            low = lowerBound(blockEnd, l)
            high = upperBound(blockStart, r) - 1

            maxPairSum = 0

            if low < high:
                firstLen = blockEnd[low] - max(blockStart[low], l) + 1
                lastLen = min(blockEnd[high], r) - blockStart[high] + 1

                if high - low == 1:
                    maxPairSum = firstLen + lastLen
                else:
                    pair1 = firstLen + blockSize[low + 1]
                    pair2 = blockSize[high - 1] + lastLen
                    rmqMaxPairSum = (
                        rmq(low + 1, high - 2, 0, 0, N - 1)
                        if low + 1 <= high - 2
                        else 0
                    )
                    maxPairSum = max(pair1, pair2, rmqMaxPairSum)

            result.append(maxPairSum + activeCount)

        return result