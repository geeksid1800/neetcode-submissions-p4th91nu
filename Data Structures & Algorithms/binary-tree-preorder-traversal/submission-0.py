from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def recur(ans, node):
            if not node:
                return
            ans.append(node.val)
            recur(ans, node.left)
            recur(ans, node.right)

        ans = []
        recur(ans, root)
        return ans