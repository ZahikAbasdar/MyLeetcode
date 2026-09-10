# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        matching_nodes_count = 0
        
        def dfs(node: TreeNode) -> tuple[int, int]:
            nonlocal matching_nodes_count
            if not node:
                return (0, 0)
            
            # Post-order traversal: compute left and right subtree stats first
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            current_sum = node.val + left_sum + right_sum
            current_count = 1 + left_count + right_count
            
            # Integer division performs the required rounding down
            if node.val == current_sum // current_count:
                matching_nodes_count += 1
                
            return (current_sum, current_count)
            
        dfs(root)
        return matching_nodes_count