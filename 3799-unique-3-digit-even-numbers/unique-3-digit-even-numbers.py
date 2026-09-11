from collections import Counter
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = Counter(digits)
        count = 0
        
        # Iterate over all possible 3-digit even numbers
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            num_freq = Counter([d1, d2, d3])
            
            # Check if all required digits are available in digits array
            if all(freq[d] >= num_freq[d] for d in num_freq):
                count += 1
                
        return count