class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = [0] * n
        stack = []
        
        # 1. Pair up matching parentheses
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
        
        # 2. Traverse and teleport through parentheses
        res = []
        curr = 0
        direction = 1  # 1 for left-to-right, -1 for right-to-left
        
        while curr < n:
            if s[curr] in '()':
                curr = pair[curr]      # Jump to the matching bracket
                direction = -direction # Reverse direction
            else:
                res.append(s[curr])
            curr += direction
            
        return "".join(res)