from collections import deque

class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        # Step 1: Find in-degree for each node
        in_degree = [0] * n
        for child in leftChild + rightChild:
            if child != -1:
                in_degree[child] += 1
                # If a node has more than one parent, it's invalid
                if in_degree[child] > 1:
                    return False
        
        # Step 2: Find the root (node with in-degree 0)
        root = -1
        for i in range(n):
            if in_degree[i] == 0:
                if root != -1:
                    return False  # More than one root found
                root = i
        
        if root == -1:
            return False  # No root found (cycle exists)
            
        # Step 3: Traverse from the root to ensure all nodes are connected and no cycles exist
        visited = set([root])
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            for child in (leftChild[node], rightChild[node]):
                if child != -1:
                    if child in visited:
                        return False  # Cycle detected
                    visited.add(child)
                    queue.append(child)
        
        # All n nodes must be visited
        return len(visited) == n