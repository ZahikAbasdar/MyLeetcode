class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        curr_depth = 0
        
        for char in s:
            if char == '(':
                curr_depth += 1
                if curr_depth > max_depth:
                    max_depth = curr_depth
            elif char == ')':
                curr_depth -= 1
                
        return max_depth