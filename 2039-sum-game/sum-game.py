class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        left_sum = sum(int(c) for c in num[:half] if c != '?')
        right_sum = sum(int(c) for c in num[half:] if c != '?')
        
        left_q = num[:half].count('?')
        right_q = num[half:].count('?')
        
        # If total number of '?' is odd, Alice can always win
        if (left_q + right_q) % 2 == 1:
            return True
        
        # Check if the extra '?' can compensate for the sum difference
        # Equation: left_sum - right_sum == (right_q - left_q) * 9 / 2
        return (left_sum - right_sum) * 2 != (right_q - left_q) * 9