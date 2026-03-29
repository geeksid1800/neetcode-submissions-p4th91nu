"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def clone(ogNode):
            #returns a deep copy of ogNode if it already exists, otherwise creates and returns it
            if not ogNode:
                return None
            if ogNode in mapping:
                return mapping[ogNode]
            copy = Node(ogNode.val)
            mapping[ogNode] = copy
            for nbr in ogNode.neighbors:
                nbrCopy = clone(nbr)
                copy.neighbors.append(nbrCopy)
            return copy
        
        mapping = dict()
        return clone(node)