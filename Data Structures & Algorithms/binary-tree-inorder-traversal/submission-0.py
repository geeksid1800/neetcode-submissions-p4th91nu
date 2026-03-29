# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def recur(ans, node):
    if not node:
        return
    recur(ans, node.left)
    ans.append(node.val)
    recur(ans,node.right)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        recur(ans, root)
        return ans