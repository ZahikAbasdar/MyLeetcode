class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        count = 1  # Start with 1 since the string will at least form one partition
        
        for char in s:
            # If character is already in the current partition, start a new one
            if char in seen:
                count += 1
                seen.clear()
            
            # Add the character to the current partition
            seen.add(char)
            
        return count