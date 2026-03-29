'''
Mixture of Standard DFS + Knapsack style greedy approach in the recursion
If we choose to rob the current node, we have no choice: we can't rob either child.
If we choose not to rob current, we still have a choice: choose to rob either child or not. 
In this case, we simply choose the option that maximises our loot.

To know how much we get from the current node, we thus need to know answer for both cases:
what we get when we rob node.left and don't rob node.left, as well as how much we get when we rob
node.right as well as when we don't rob node.right. So for each recursive problem, we return 2 values:
What we get when we chose to rob the current node, and what we get when we chose not to.  
'''
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(currNode):
            if not currNode:
                return 0,0
            
            stealL, noStealL = dfs(currNode.left)
            stealR, noStealR = dfs(currNode.right)

            stealCurr = currNode.val + noStealL + noStealR
            noStealCurr = max(stealL, noStealL) + max(stealR, noStealR)
            
            return stealCurr, noStealCurr

        return max(dfs(root))