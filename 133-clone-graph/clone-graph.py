"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return None

        if node in self.visited:
            return self.visited[node]

    # Create clone and record in visited map
        clone = Node(node.val)
        self.visited[node] = clone

    # Recursively copy all neighbor connections
        for neighbor in node.neighbors:
            clone.neighbors.append(self.cloneGraph(neighbor))

        return clone