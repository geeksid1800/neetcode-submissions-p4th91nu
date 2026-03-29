'''
Given any two nodes N1 and N2, the distance between them will depend on their common ancestor (say, R).
dist(N1, N2) = dist(N1, R) + dis(N2, R), where dist(x,R) will simply be the depth of node x from R.
That means for any node N, the diameter of the subtree rooted at N will be given by 
depth(N.left) + depth(N.right).
The problem has thus been transformed into finding the depth of each node recursively, while maintaining
a global max variable. 
'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0
        
        def depth(node):
            if not node:
                return 0
            
            lDepth = depth(node.left)
            rDepth = depth(node.right)
            
            nodeDepth = max(lDepth, rDepth) + 1
            self.dia = max(self.dia, lDepth + rDepth)
            return nodeDepth
        
        depth(root)
        return self.dia