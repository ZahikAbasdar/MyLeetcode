class Solution:

    def countCommas(self, n: int) -> int:
        total_commas = 0
        start = 1000
        commas = 1

        while start <= n:
            next_start = start * 1000
            count = min(n, next_start - 1) - start + 1
            total_commas += count * commas

            start = next_start
            commas += 1

        return total_commas