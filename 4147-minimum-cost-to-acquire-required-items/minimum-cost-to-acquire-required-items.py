class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Hint 1: For the overlapping part min(need1, need2), choose the cheapest way to satisfy both.
        # We can either use a type 3 item (costBoth) or one type 1 and one type 2 item (cost1 + cost2).
        common_count = min(need1, need2)
        total_cost = common_count * min(costBoth, cost1 + cost2)
        
        # Remaining needs after satisfying the common requirement
        rem1 = need1 - common_count
        rem2 = need2 - common_count
        
        # Hint 2: For remaining type 1 requirements, use the cheaper option between costBoth and cost1
        if rem1 > 0:
            total_cost += rem1 * min(costBoth, cost1)
            
        # Hint 3: For remaining type 2 requirements, use the cheaper option between costBoth and cost2
        if rem2 > 0:
            total_cost += rem2 * min(costBoth, cost2)
            
        return total_cost