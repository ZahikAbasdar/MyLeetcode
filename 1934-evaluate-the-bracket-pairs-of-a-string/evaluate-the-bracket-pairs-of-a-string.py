class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        lookup = dict(knowledge)
        parts = s.split('(')
        
        # The first element is the prefix before the first '('
        res = [parts[0]]
        
        for part in parts[1:]:
            key, rest = part.split(')')
            res.append(lookup.get(key, '?'))
            res.append(rest)
            
        return "".join(res)