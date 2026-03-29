# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        q = deque()
        q.append([root, 1]) #[node, level]
        level, currLevel = 1, []
        while q:
            node, nodeLevel = q.popleft()
            if nodeLevel > level:
                level += 1
                ans.append(currLevel)
                currLevel = []
            currLevel.append(node.val)
            if node.left:
                q.append([node.left, nodeLevel+1])
            if node.right:
                q.append([node.right, nodeLevel+1])                
        
        ans.append(currLevel)
        return ans