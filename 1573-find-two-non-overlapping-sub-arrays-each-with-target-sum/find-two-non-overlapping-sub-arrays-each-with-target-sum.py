class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        # min_len[i] will store the minimum length of a valid subarray ending at or before index i
        min_len = [float('inf')] * n
        ans = float('inf')
        left = 0
        current_sum = 0
        best_so_far = float('inf')
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink the window from the left if the sum exceeds the target
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
                
            # If we found a subarray with the target sum
            if current_sum == target:
                curr_length = right - left + 1
                
                # Check if there is a valid non-overlapping subarray before our current 'left' index
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, curr_length + min_len[left - 1])
                
                # Update the best length seen so far
                best_so_far = min(best_so_far, curr_length)
            
            # Record the minimum length found up to the current right pointer
            min_len[right] = best_so_far
            
        return ans if ans != float('inf') else -1