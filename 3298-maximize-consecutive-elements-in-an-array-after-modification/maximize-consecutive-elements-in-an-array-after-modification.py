from typing import List


class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        ans = 0

        for x in nums:
            # Option 1: increment x -> x + 1, extending sequence ending at x
            dp[x + 1] = dp.get(x, 0) + 1
            # Option 2: keep x as x, extending sequence ending at x - 1
            dp[x] = dp.get(x - 1, 0) + 1

            ans = max(ans, dp[x + 1], dp[x])

        return ans