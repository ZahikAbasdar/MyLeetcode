class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((123 - ord(c)) * (i + 1) for i, c in enumerate(s))