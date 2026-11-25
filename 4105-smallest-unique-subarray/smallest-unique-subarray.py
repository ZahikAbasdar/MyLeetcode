from collections import Counter
from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        BASE1, MOD1 = 1315423911, (1 << 61) - 1
        BASE2, MOD2 = 2654435761, 10**9 + 7

        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)

        for i, x in enumerate(nums):
            val = x + 1
            p1[i + 1] = (p1[i] * BASE1) % MOD1
            p2[i + 1] = (p2[i] * BASE2) % MOD2
            pref1[i + 1] = (pref1[i] * BASE1 + val) % MOD1
            pref2[i + 1] = (pref2[i] * BASE2 + val) % MOD2

        def get_hash(left: int, right: int) -> tuple[int, int]:
            length = right - left
            h1 = (pref1[right] - pref1[left] * p1[length]) % MOD1
            h2 = (pref2[right] - pref2[left] * p2[length]) % MOD2
            return (h1, h2)

        def has_unique_of_length(length: int) -> bool:
            counts = Counter(
                get_hash(i, i + length) for i in range(n - length + 1)
            )
            return any(freq == 1 for freq in counts.values())

        lo, hi = 1, n
        ans = n

        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique_of_length(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans