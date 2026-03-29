'''
Mixture of Standard DFS + Knapsack style greedy approach in the recursion
If a node's parent has been chosen, we have no choice: we can't rob (choose) current node
If parent hasn't been robbed, we still have a choice on whether to rob current node or not.
In that case, answer will be whichever case maximises the loot. 

Added memoization to not get TLE.
'''
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.cache = {}
        def dfs(node, prevChosen):
            #prevChosen is True if node's parent has been robbed (so node is not eligible)
            if not node:
                return 0
            if (node, prevChosen) in self.cache:
                return self.cache[(node, prevChosen)]

            if prevChosen:
                nodeNotChosen = dfs(node.left, False) + dfs(node.right, False)
                self.ans = max(self.ans, nodeNotChosen)
                self.cache[(node, prevChosen)] = nodeNotChosen
                return nodeNotChosen
            else:
                #parent was not chosen, we are free to pick this node or not
                nodeChosen = node.val + dfs(node.left, True) + dfs(node.right, True)
                nodeNotChosen = dfs(node.left, False) + dfs(node.right, False)
                self.ans = max(self.ans, nodeChosen, nodeNotChosen)
                self.cache[(node, prevChosen)] = max(nodeChosen, nodeNotChosen)
                return max(nodeChosen, nodeNotChosen)
        
        dfs(root, False)
        return self.ans