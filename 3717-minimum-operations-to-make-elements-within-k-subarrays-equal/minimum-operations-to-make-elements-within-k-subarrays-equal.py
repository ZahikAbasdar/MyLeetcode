import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        
        max_heap = [] # stores smaller half (store elements as negative for max-heap)
        min_heap = [] # stores larger half
        
        rem_max = {}
        rem_min = {}
        
        size_max = 0
        size_min = 0
        
        sum_max = 0
        sum_min = 0
        
        def add(val):
            nonlocal size_max, size_min, sum_max, sum_min
            if not max_heap or val <= -max_heap[0]:
                heapq.heappush(max_heap, -val)
                sum_max += val
                size_max += 1
            else:
                heapq.heappush(min_heap, val)
                sum_min += val
                size_min += 1
            balance_heaps()

        def remove(val):
            nonlocal size_max, size_min, sum_max, sum_min
            if max_heap and val <= -max_heap[0]:
                rem_max[val] = rem_max.get(val, 0) + 1
                sum_max -= val
                size_max -= 1
            else:
                rem_min[val] = rem_min.get(val, 0) + 1
                sum_min -= val
                size_min -= 1
            balance_heaps()

        def balance_heaps():
            nonlocal size_max, size_min, sum_max, sum_min
            while max_heap and rem_max.get(-max_heap[0], 0) > 0:
                val = -heapq.heappop(max_heap)
                rem_max[val] -= 1
            while min_heap and rem_min.get(min_heap[0], 0) > 0:
                val = heapq.heappop(min_heap)
                rem_min[val] -= 1

            target_max = (x + 1) // 2
            target_min = x // 2

            while size_max > target_max:
                val = -heapq.heappop(max_heap)
                sum_max -= val
                size_max -= 1
                heapq.heappush(min_heap, val)
                sum_min += val
                size_min += 1
                while max_heap and rem_max.get(-max_heap[0], 0) > 0:
                    v = -heapq.heappop(max_heap)
                    rem_max[v] -= 1

            while size_max < target_max and min_heap:
                val = heapq.heappop(min_heap)
                sum_min -= val
                size_min -= 1
                heapq.heappush(max_heap, -val)
                sum_max += val
                size_max += 1
                while min_heap and rem_min.get(min_heap[0], 0) > 0:
                    v = heapq.heappop(min_heap)
                    rem_min[v] -= 1

        costs = [0] * (n - x + 1)
        
        # Initialize first window
        for i in range(x):
            add(nums[i])
            
        median = -max_heap[0]
        costs[0] = (size_max * median - sum_max) + (sum_min - size_min * median)
        
        # Slide the window
        for i in range(1, n - x + 1):
            remove(nums[i - 1])
            add(nums[i + x - 1])
            
            median = -max_heap[0]
            costs[i] = (size_max * median - sum_max) + (sum_min - size_min * median)

        # Step 2: DP to pick k non-overlapping windows
        INF = float('inf')
        dp_table = [[INF] * (n + 1) for _ in range(k + 1)]
        for i in range(n + 1):
            dp_table[0][i] = 0
            
        for j in range(1, k + 1):
            for i in range(j * x, n + 1):
                option1 = dp_table[j][i - 1]
                prev_cost = dp_table[j - 1][i - x] if i >= x else INF
                window_cost = costs[i - x] if (i - x >= 0 and i - x < len(costs)) else INF
                
                option2 = prev_cost + window_cost if prev_cost != INF and window_cost != INF else INF
                dp_table[j][i] = min(option1, option2)
                
        return dp_table[k][n] if dp_table[k][n] != INF else -1