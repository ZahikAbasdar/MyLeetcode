class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum(int(d) for d in str(n))
        
        n = len(nums)
        # Pair each number with its (digit_sum, value, original_index)
        indexed_nums = []
        for i, val in enumerate(nums):
            indexed_nums.append((digit_sum(val), val, i))
        
        # Sort based on digit sum, then by value (as a tiebreaker)
        sorted_nums = sorted(indexed_nums, key=lambda x: (x[0], x[1]))
        
        # Find the minimum swaps to sort the array using cycle decomposition
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if visited[i] or sorted_nums[i][2] == i:
                continue
            
            # Count the size of the cycle
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = sorted_nums[curr][2]
                cycle_size += 1
            
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        return swaps