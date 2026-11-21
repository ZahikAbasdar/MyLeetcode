from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        orig_tree: List[List[int]] = [[] for _ in range(n)]
        for i in range(1, n):
            orig_tree[parent[i]].append(i)

        # Tracks the most recent ancestor index for each character 'a'..'z'
        last_seen: List[int] = [-1] * 26
        new_parent: List[int] = parent[:]

        def assign_new_parents(node: int) -> None:
            char_idx = ord(s[node]) - ord('a')
            prev_ancestor = last_seen[char_idx]

            # If a closer ancestor with the same character exists, switch parent
            if prev_ancestor != -1 and node != 0:
                new_parent[node] = prev_ancestor

            # Push current node as the newest ancestor for its character
            last_seen[char_idx] = node
            for child in orig_tree[node]:
                assign_new_parents(child)

            # Backtrack so sibling branches don't see this node as an ancestor
            last_seen[char_idx] = prev_ancestor

        assign_new_parents(0)

        new_tree: List[List[int]] = [[] for _ in range(n)]
        for i in range(1, n):
            new_tree[new_parent[i]].append(i)

        ans: List[int] = [0] * n

        def compute_sizes(node: int) -> int:
            size = 1
            for child in new_tree[node]:
                size += compute_sizes(child)
            ans[node] = size
            return size

        compute_sizes(0)
        return ans