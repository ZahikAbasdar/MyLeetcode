class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)
        min_odd = float('inf')
        
        for x in nums1:
            if x % 2 != 0:
                min_odd = min(min_odd, x)
                
        # Case 1: All elements can be made ODD
        # This is possible if and only if the smallest element in nums1 is odd.
        if min_val % 2 != 0:
            return True
            
        # Case 2: All elements can be made EVEN
        # If min_val is even, any even number is fine.
        # For any odd number x, we need a smaller odd number (min_odd < x) to subtract.
        for x in nums1:
            if x % 2 != 0 and x <= min_odd:
                # If there's an odd number that doesn't have a strictly smaller odd number,
                # it cannot be turned into an even number.
                return False
                
        return True