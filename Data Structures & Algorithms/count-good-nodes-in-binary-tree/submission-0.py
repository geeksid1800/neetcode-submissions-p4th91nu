# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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
            