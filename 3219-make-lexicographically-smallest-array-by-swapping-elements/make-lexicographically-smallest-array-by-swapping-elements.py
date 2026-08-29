from collections import deque
from typing import List


class Solution:

    def lexicographicallySmallestArray(
        self, nums: List[int], limit: int
    ) -> List[int]:
        n = len(nums)

        # Pair each number with its original index and sort by value
        sorted_nums = sorted((val, idx) for idx, val in enumerate(nums))

        groups = []
        val_to_group = {}

        # Divide into connected components
        for val, idx in sorted_nums:
            if not groups or val - groups[-1][-1] > limit:
                groups.append(deque())

            groups[-1].append(val)
            val_to_group[val] = len(groups) - 1

        # Reconstruct the answer array
        res = [0] * n
        for i in range(n):
            val = nums[i]
            group_idx = val_to_group[val]

            # Pop the smallest remaining element for this component
            res[i] = groups[group_idx].popleft()

        return res