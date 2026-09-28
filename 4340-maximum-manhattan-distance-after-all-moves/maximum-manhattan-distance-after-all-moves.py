class Solution:
    def maxDistance(self, moves: str) -> int:
        x = abs(moves.count('R') - moves.count('L'))
        y = abs(moves.count('U') - moves.count('D'))
        return x + y + moves.count('_')