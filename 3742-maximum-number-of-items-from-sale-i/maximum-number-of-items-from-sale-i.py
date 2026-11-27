from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_factor = max(factor for factor, _ in items)

        # Count how many items exist for each exact factor value
        freq = [0] * (max_factor + 1)
        for factor, _ in items:
            freq[factor] += 1

        # mult_count[d] = total items whose factor is divisible by d
        mult_count = [0] * (max_factor + 1)
        for d in range(1, max_factor + 1):
            total = 0
            for multiple in range(d, max_factor + 1, d):
                total += freq[multiple]
            mult_count[d] = total

        # dp[b] = maximum total copies (purchased + free) using at most budget b
        dp = [0] * (budget + 1)

        for factor, price in items:
            if price > budget:
                continue

            # Exclude the item itself (j != i)
            free_bonus = mult_count[factor] - 1

            # 1. First copy: 0/1 transition (reverse order prevents double-counting free_bonus)
            for b in range(budget, price - 1, -1):
                candidate = dp[b - price] + 1 + free_bonus
                if candidate > dp[b]:
                    dp[b] = candidate

            # 2. Additional copies: unbounded transition (forward order)
            for b in range(price, budget + 1):
                candidate = dp[b - price] + 1
                if candidate > dp[b]:
                    dp[b] = candidate

        return max(dp)