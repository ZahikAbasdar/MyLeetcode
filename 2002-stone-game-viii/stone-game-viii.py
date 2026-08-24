class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        from itertools import accumulate
from typing import List


class Solution:

    def stoneGameVIII(self, stones: List[int]) -> int:
        # Calculate prefix sums of the stones
        pref = list(accumulate(stones))

        # Base case: taking all stones gives pref[-1], with no remaining stones for the next player
        ans = pref[-1]

        # Iterate backwards from index n-2 down to 1 (representing taking x stones, where x = i + 1)
        # At each step, the player can either choose to take x stones (gaining pref[i] - ans)
        # or skip and let a future optimal choice prevail.
        for i in range(len(stones) - 2, 0, -1):
            ans = max(ans, pref[i] - ans)

        return ans