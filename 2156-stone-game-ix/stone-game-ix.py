class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0] * 3
        for stone in stones:
            cnt[stone % 3] += 1
            
        c0, c1, c2 = cnt[0], cnt[1], cnt[2]
        
       
        if c0 % 2 == 0:
            return c1 >= 1 and c2 >= 1
        
        # If c0 is odd, Alice wins if the absolute difference 
        # between 1s and 2s is strictly greater than 2.
        return abs(c1 - c2) > 2