from collections import defaultdict

class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        subarray_counts = defaultdict(int)

        # Iterate over all subarrays of length k
        for i in range(n - k + 1):
            # Collect unique elements in the current subarray
            unique_in_subarray = set(nums[i:i + k])
            for num in unique_in_subarray:
                subarray_counts[num] += 1

        # Find the maximum element present in exactly 1 subarray
        ans = -1
        for num, count in subarray_counts.items():
            if count == 1:
                ans = max(ans, num)

        return ans