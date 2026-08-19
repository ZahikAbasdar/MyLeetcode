from collections import defaultdict

class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        # Map row -> bitmask of reserved seats (for seats 2 to 9)
        row_reserved = defaultdict(int)
        
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                # Use (seat - 2) to fit seats 2-9 into bits 0-7
                row_reserved[row] |= (1 << (seat - 2))
        
        # Start by assuming all rows can hold 2 groups
        max_groups = n * 2
        
        # Bitmasks representing collision with groups
        # Seats 2,3,4,5  -> bits 0,1,2,3 -> 0b00001111 (15)
        # Seats 6,7,8,9  -> bits 4,5,6,7 -> 0b11110000 (240)
        # Seats 4,5,6,7  -> bits 2,3,4,5 -> 0b00111100 (60)
        left_mask = 0b00001111
        right_mask = 0b11110000
        middle_mask = 0b00111100

        for row, mask in row_reserved.items():
            left_available = (mask & left_mask) == 0
            right_available = (mask & right_mask) == 0
            
            if left_available and right_available:
                # Both blocks are free, no group reduction needed
                continue
            elif left_available or right_available or (mask & middle_mask) == 0:
                # Exactly 1 block can be placed (left, right, or middle)
                max_groups -= 1
            else:
                # No blocks can be placed in this row
                max_groups -= 2
                
        return max_groups