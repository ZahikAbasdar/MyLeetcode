class Solution(object):
    def concatenatedDivisibility(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Sort nums to construct the answer in lexicographical order
        nums.sort()
        n = len(nums)
        
        # Precompute (10^(length of nums[i])) % k for each number
        mult = [10 ** len(str(x)) % k for x in nums]
        
        # Memoization table: memo[mask][rem] = True/False
        memo = {}

        def can_form(mask, rem):
            if mask == (1 << n) - 1:
                return rem == 0
            
            state = (mask, rem)
            if state in memo:
                return memo[state]
            
            for i in range(n):
                if not (mask & (1 << i)):
                    next_rem = (rem * mult[i] + nums[i]) % k
                    if can_form(mask | (1 << i), next_rem):
                        memo[state] = True
                        return True
            
            memo[state] = False
            return False

        # If no valid permutation can form a number divisible by k
        if not can_form(0, 0):
            return []

        # Reconstruct the lexicographically smallest path greedily
        res = []
        mask = 0
        rem = 0

        for _ in range(n):
            for i in range(n):
                if not (mask & (1 << i)):
                    next_rem = (rem * mult[i] + nums[i]) % k
                    if can_form(mask | (1 << i), next_rem):
                        res.append(nums[i])
                        mask |= (1 << i)
                        rem = next_rem
                        break

        return res