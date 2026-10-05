class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                v = stack.pop()
                # If v is 0, it means we closed a "()", which has score 1.
                # Otherwise, it means we closed "(A)", so the score is 2 * v.
                score = 1 if v == 0 else 2 * v
                stack[-1] += score
                
        return stack[0]