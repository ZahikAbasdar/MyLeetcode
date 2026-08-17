class Solution(object):
    def largestMultipleOfThree(self, digits):
        """
        :type digits: List[int]
        :rtype: str
        """
        # Group digits by their remainder when divided by 3
        mod0 = []
        mod1 = []
        mod2 = []
        
        for d in sorted(digits):
            if d % 3 == 0:
                mod0.append(d)
            elif d % 3 == 1:
                mod1.append(d)
            else:
                mod2.append(d)
                
        total_sum = sum(digits)
        remainder = total_sum % 3
        
        # Adjust lists based on the remainder to make the sum divisible by 3
        if remainder == 1:
            if mod1:
                mod1.pop(0)  # Remove smallest element with remainder 1
            elif len(mod2) >= 2:
                mod2.pop(0)  # Remove two smallest elements with remainder 2
                mod2.pop(0)
            else:
                return ""
        elif remainder == 2:
            if mod2:
                mod2.pop(0)  # Remove smallest element with remainder 2
            elif len(mod1) >= 2:
                mod1.pop(0)  # Remove two smallest elements with remainder 1
                mod1.pop(0)
            else:
                return ""
                
        # Combine remaining digits and sort in descending order
        res = sorted(mod0 + mod1 + mod2, reverse=True)
        
        if not res:
            return ""
        
        # Handle leading zero edge case (e.g., [0, 0, 0] -> "0")
        if res[0] == 0:
            return "0"
            
        return "".join(map(str, res))