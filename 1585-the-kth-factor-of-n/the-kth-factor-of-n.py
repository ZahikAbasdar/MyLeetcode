class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        
        # Iterating up to sqrt(n)
        i = 1
        while i * i <= n:
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i
                factors.append(i)
            i += 1
            
        # Handle exact square roots to avoid counting the middle factor twice
        if factors and factors[-1] * factors[-1] == n:
            factors.pop()
            
        # Check remaining larger paired factors in reverse order
        if k <= len(factors):
            return n // factors[-k]
            
        return -1