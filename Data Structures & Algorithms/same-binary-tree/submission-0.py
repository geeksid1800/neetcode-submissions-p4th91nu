# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def recur(p, q):
            if not (p or q): 
                return True #if both nodes are None
            if not (p and q):
                return False #if exactly one node is None

            return (p.val == q.val) and recur(p.left, q.left) and recur(p.right, q.right)
        
        return recur(root1, root2)
