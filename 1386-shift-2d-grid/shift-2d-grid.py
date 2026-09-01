class Solution:

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n

        # Reduce k to avoid redundant full grid rotations
        k = k % total

        # Flatten grid into a 1D list
        flat = [grid[r][c] for r in range(m) for c in range(n)]

        # Perform the right shift by k positions
        shifted = flat[-k:] + flat[:-k]

        # Reconstruct the 2D grid from the shifted 1D list
        return [shifted[i * n : (i + 1) * n] for i in range(m)]