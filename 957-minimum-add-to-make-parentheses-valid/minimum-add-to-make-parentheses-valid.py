class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        min_adds = 0
        
        for char in s:
            if char == '(':
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    min_adds += 1
                    
        return min_adds + open_brackets