from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        # result[x] will store the total count of valid subarrays with remainder x
        result = [0] * k
        
        # dp[r] stores the count of subarrays ending at the PREVIOUS index with remainder r
        dp = [0] * k
        
        for num in nums:
            # next_dp[r] will store the count of subarrays ending at the CURRENT index with remainder r
            next_dp = [0] * k
            
            # Extend existing subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * num) % k
                    next_dp[new_r] += dp[r]
            
            # Start a new subarray with just the current element
            next_dp[num % k] += 1
            
            # Add the current index's valid subarrays to our total result
            for r in range(k):
                result[r] += next_dp[r]
                
            # Move to the next index
            dp = next_dp
            
        return result