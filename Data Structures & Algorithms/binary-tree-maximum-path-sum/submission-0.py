'''
For any given node and the subtree rooted at it, there are 3 ways for the node to be part of a path:
1) path starts at root, goes down to left subtree in one long chain
2) path starts at root, goes down to right subtree in one long chain
3) path has a turning point at root, goes from left subtree to root to right subtree.
Only (1) and (2) have potential to be extended further upwards (parent of current node), 3rd option
cannot be a part of any bigger solutions. So in the DFS, we will maintain a global self.ans to
compare all options, but our recursive function call will only return the results of (1) or (2).
'''
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')
        def dfs(root):
            if not root:
                return float('-inf')
            leftMax = max(dfs(root.left), 0) #choose path left and down only if it is positive
            rightMax = max(dfs(root.right), 0) #choose path right and down only if it is positive
            self.ans = max(self.ans, root.val+leftMax, root.val+rightMax, root.val+leftMax+rightMax)
            return max(root.val+leftMax, root.val+rightMax)
        
        dfs(root)
        return self.ans