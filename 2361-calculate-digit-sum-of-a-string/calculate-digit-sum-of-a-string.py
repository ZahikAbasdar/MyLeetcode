class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # Continue rounds as long as the length of s is greater than k
        while len(s) > k:
            new_s = []
            
            # Divide s into consecutive groups of size k
            for i in range(0, len(s), k):
                group = s[i:i + k]
                # Calculate the sum of all digits in the group
                total_sum = sum(int(digit) for digit in group)
                # Append the string representation of the sum
                new_s.append(str(total_sum))
            
            # Merge consecutive groups together to form the new string
            s = "".join(new_s)
            
        return s