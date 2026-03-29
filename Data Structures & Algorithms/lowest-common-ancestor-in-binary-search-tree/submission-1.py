'''
Lowest Common Ancestor (LCA) will be the first node where p and q are on the opposite sides of it.
Find which side of 'root' p and q are on. 
1) If p or q themselves are the root, the LCA has to be root itself
2) The first time you get p and q on different sides of root, you have an answer
'''
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        
        #now recursively try to find LCA in root.left and root.right.
        #if both are on same side, one of the two calls will be None.
        #if they are on different sides, both will be non-Null
        l, r = self.lowestCommonAncestor(root.left, p, q),self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        if l:
            return l
        if r:
            return r