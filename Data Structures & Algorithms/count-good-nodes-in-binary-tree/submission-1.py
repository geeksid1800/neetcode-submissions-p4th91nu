'''
Standard DFS solution, maintain a global self.ans variable.
Whenever you encounter a node with value greater than maxYet, increment self.ans
and update maxYet. Then recursively call the dfs function on root.left and root.right
'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        if not root:
            return self.ans
        def countGood(root, maxYet) -> None:
            if not root:
                return
            if root.val >= maxYet:
                maxYet = root.val
                self.ans += 1
            if root.left:
                countGood(root.left, maxYet)
            if root.right:
                countGood(root.right, maxYet)

        countGood(root, -100)
        return self.ans
            