class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []
        union_set = set()
        curr_set = {""}
        
        for char in expression:
            if char == '{':
                # Save current state before entering a new brace level
                stack.append((union_set, curr_set))
                union_set = set()
                curr_set = {""}
            elif char == '}':
                # Complete the current brace level and multiply with the previouscurr_set
                brace_result = union_set | curr_set
                prev_union, prev_curr = stack.pop()
                curr_set = {a + b for a in prev_curr for b in brace_result}
                union_set = prev_union
            elif char == ',':
                # Add current product to the union and reset curr_set for the next part
                union_set |= curr_set
                curr_set = {""}
            else:
                # Multiply current set with the single character
                curr_set = {a + char for a in curr_set}
                
        return sorted(union_set | curr_set)