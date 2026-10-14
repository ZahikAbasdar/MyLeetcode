class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Check if it's possible to form the number with the given sum and length
        if sum < 0 or sum > 9 * num:
            return ""
        
        res = []
        for i in range(num):
            # Take as much as possible for the current digit, leaving enough for the remaining positions
            curr = min(9, sum)
            res.append(str(curr))
            sum -= curr
            
        return "".join(res)