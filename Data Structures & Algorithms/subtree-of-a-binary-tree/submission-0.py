'''
There are 3 ways in which subRoot can be a subtree of root:
1) root and subRoot are identical trees
2) subRoot is a subtree of root.left
3) subRoot is a subtree of root.right
'''
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if not (p or q):
                return True #both are None
            if not (p and q):
                return False #exactly one is None
            return (p.val==q.val) and isSame(p.left, q.left) and isSame(p.right, q.right)
        
        if not subRoot:
            return True #None is automatically a subtree of everything
        if not root:
            return False #subRoot exists but root doesn't
        
        return isSame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)