# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        # Dictionary to store the roots of available trees for O(1) lookup
        roots = {t.val: t for t in trees}
        leaves = set()
        
        # Collect all leaf values
        for t in trees:
            if t.left:
                leaves.add(t.left.val)
            if t.right:
                leaves.add(t.right.val)
                
        # The final root is the one that is never a leaf in any other tree
        candidate_root = None
        for t in trees:
            if t.val not in leaves:
                candidate_root = t
                break
                
        # If there's no valid root, or multiple disjoint cycles, return None
        if not candidate_root:
            return None
            
        # Remove the candidate root from our available roots pool to avoid self-merging
        del roots[candidate_root.val]
        
        # DFS to merge trees and validate the BST property simultaneously
        def dfs(node, min_val, max_val):
            if not node:
                return True
            
            # Violates BST bounds
            if not (min_val < node.val < max_val):
                return False
                
            # If we are at a leaf node and there is a tree we can merge here
            if not node.left and not node.right:
                if node.val in roots:
                    # Pop the tree from roots and attach its children
                    nxt_tree = roots.pop(node.val)
                    node.left = nxt_tree.left
                    node.right = nxt_tree.right
                    
            # Continue validating down the left and right subtrees
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)
        
        # If the tree is a valid BST and we used exactly all given trees
        if dfs(candidate_root, float('-inf'), float('inf')) and len(roots) == 0:
            return candidate_root
            
        return None