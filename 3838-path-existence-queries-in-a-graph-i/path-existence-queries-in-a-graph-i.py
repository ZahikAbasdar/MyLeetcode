class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # comp[i] stores the component ID for node i
        comp = [0] * n
        
        # Preprocess connected components in O(n)
        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                comp[i] = comp[i - 1]
            else:
                comp[i] = comp[i - 1] + 1
        
        # Answer each query in O(1)
        res = []
        for u, v in queries:
            res.append(comp[u] == comp[v])
            
        return res