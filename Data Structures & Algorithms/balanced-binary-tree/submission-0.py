'''
Very similar to #543. Diameter of Binary Tree
Maintain a global boolean flag (self.balanced).
At each node, calculate the depth of left and right subtrees recursively.
If left depth and right depth have difference of more than 1, make the flag false
'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def depth(node):
            if not node:
                return 0
            lDepth, rDepth = depth(node.left), depth(node.right)
            if abs(lDepth - rDepth) > 1: 
                self.balanced = False

            return 1 + max(lDepth, rDepth) 

        self.balanced = True
        depth(root)
        return self.balanced