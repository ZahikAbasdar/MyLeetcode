class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def backtrack(current: str, open_count: int, close_count: int):
            # Base case: when the string reaches the maximum length (2 * n)
            if len(current) == 2 * n:
                res.append(current)
                return
            
            # Rule 1: We can add an opening bracket if we haven't used all n of them
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
                
            # Rule 2: We can add a closing bracket if it won't exceed the number of open brackets
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
                
        backtrack("", 0, 0)
        return res