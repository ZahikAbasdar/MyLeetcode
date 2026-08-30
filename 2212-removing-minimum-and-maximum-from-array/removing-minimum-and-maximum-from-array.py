class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        # Find indices of min and max elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Ensure idx1 is smaller (leftmost) and idx2 is larger (rightmost)
        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # 1. Both from front: cost to reach rightmost element
        both_front = right + 1

        # 2. Both from back: cost to reach leftmost element from right end
        both_back = n - left

        # 3. One from front, one from back
        front_and_back = (left + 1) + (n - right)

        return min(both_front, both_back, front_and_back)