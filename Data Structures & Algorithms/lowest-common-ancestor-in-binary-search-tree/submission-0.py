'''
Possible approach:
Lowest Common Ancestor (LCA) will be the first node where p and q are on the opposite sides of it.
Find which side of 'root' p and q are on. 
1) If p or q themselves are the root, the LCA has to be root itself
2) The first time you get p and q on different sides of root, you have an answer
'''
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if (p.val==root.val) or (q.val==root.val):
            return root
        
        def findNode(root, node) -> bool:
            # return True if you find node in subtree of root 
            if not node: return True
            if not root: return False
            return (node.val==root.val) or findNode(root.left, node) or findNode(root.right, node)
        
        
        #if we reached this point, that means neither p nor q are 'root' itself
        #now check if p and q are on same side of root, if so recur downwards
        #i.e. they have a common ancestor further down
        pFoundLeft, qFoundLeft = findNode(root.left, p), findNode(root.left, q)
        print(f"{root.val=}, {pFoundLeft=}, {qFoundLeft=}")
        if pFoundLeft and qFoundLeft:
            return self.lowestCommonAncestor(root.left, p, q)
        elif not (pFoundLeft or qFoundLeft):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            # one of p,q is found on left side of root and other on right side
            return root