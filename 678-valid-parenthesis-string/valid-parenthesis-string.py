class Solution:
    def checkValidString(self, s: str) -> bool:
        # 'low' tracks the minimum possible number of unmatched '('
        # 'high' tracks the maximum possible number of unmatched '('
        low = 0
        high = 0
        
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:  # char == '*'
                low -= 1   # Treat '*' as ')'
                high += 1  # Treat '*' as '('
            
            # If high < 0, even treating all '*' as '(' cannot balance the ')'
            if high < 0:
                return False
            
            # We cannot have fewer than 0 open parentheses, so reset low to 0
            # (meaning we treat some previous '*' as empty strings instead of ')')
            low = max(low, 0)
            
        # The string is valid if we can reach 0 unmatched '(' at the end
        return low == 0