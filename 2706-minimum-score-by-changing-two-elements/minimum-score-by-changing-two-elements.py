class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        
        # Since we can make two elements equal, the minimum absolute difference
        # ("low" score) can always be reduced to 0.
        # To minimize the maximum difference ("high" score), we effectively drop
        # two extreme elements from the sorted array and take the minimum span
        # among the three remaining choices:
        # 1. Drop the two smallest elements: nums[-1] - nums[2]
        # 2. Drop the two largest elements:  nums[-3] - nums[0]
        # 3. Drop one smallest and one largest: nums[-2] - nums[1]
        return min(
            nums[-1] - nums[2],
            nums[-3] - nums[0],
            nums[-2] - nums[1]
        )