"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
"""
Core of this problem involves a hashset mapping the original nodes to their deep copies.
When we create a copy node, we map it to it's original.
Then we recursively create it's neighbors and set the cloned neighbors as copy's neighbors
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapping = dict()
        def getOrCreate(ogNode):
            if not ogNode: return None
            if ogNode in mapping: return mapping[ogNode]
            copyNode = Node(val=ogNode.val)
            mapping[ogNode] = copyNode

            for neighbor in ogNode.neighbors:
                copyNeighbor = getOrCreate(neighbor)
                copyNode.neighbors.append(copyNeighbor)
            
            return copyNode
        
        return getOrCreate(node) if node else None