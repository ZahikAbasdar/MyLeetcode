from collections import deque
from typing import List


class Solution:

    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        start_x, start_y = -1, -1
        litter_locations = []

        # Find starting position and all litter locations
        for r in range(m):
            for c in range(n):
                cell = classroom[r][c]
                if cell == "S":
                    start_x, start_y = r, c
                elif cell == "L":
                    litter_locations.append((r, c))

        num_litter = len(litter_locations)
        full_mask = (1 << num_litter) - 1

        # Map each litter position to a bit index for state tracking
        litter_map = {pos: i for i, pos in enumerate(litter_locations)}

        # Track the maximum remaining energy seen for state: (row, col, collected_litter_mask)
        best_energy = {}

        # BFS queue stores tuples: (r, c, mask, current_energy, steps)
        queue = deque([(start_x, start_y, 0, energy, 0)])
        best_energy[(start_x, start_y, 0)] = energy

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c, mask, e, steps = queue.popleft()

            # Target reached: all litters collected
            if mask == full_mask:
                return steps

            # If energy reaches 0, we can only continue if currently at a reset area 'R'
            if e == 0:
                if classroom[r][c] == "R":
                    e = energy
                else:
                    continue

            # Prune state if we have reached (r, c, mask) with strictly higher energy before
            if e < best_energy.get((r, c, mask), -1):
                continue

            # Explore all 4 adjacent moves
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != "X":
                    new_e = e - 1
                    new_mask = mask

                    # Pick up litter if present
                    if classroom[nr][nc] == "L" and (nr, nc) in litter_map:
                        new_mask |= 1 << litter_map[(nr, nc)]

                    # If landing on 'R', restore energy immediately
                    if classroom[nr][nc] == "R":
                        new_e = energy

                    # Only process this path if it gives strictly better energy for this state
                    if new_e > best_energy.get((nr, nc, new_mask), -1):
                        best_energy[(nr, nc, new_mask)] = new_e
                        queue.append((nr, nc, new_mask, new_e, steps + 1))

        return -1