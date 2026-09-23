class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        
        # If the total sum is less than x, it's impossible
        if target < 0:
            return -1
            
        # If the target is exactly 0, we need to remove all elements
        if target == 0:
            return len(nums)
            
        max_len = -1
        current_sum = 0
        left = 0
        
        # Sliding window to find the longest subarray with sum == target
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink the window if the sum exceeds the target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            # Update max_len if we find a valid subarray
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
                
        # If max_len is still -1, no valid subarray was found
        return len(nums) - max_len if max_len != -1 else -1