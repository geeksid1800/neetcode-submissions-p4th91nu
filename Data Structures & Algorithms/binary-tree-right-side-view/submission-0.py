from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        q = deque()
        q.append([root, 1]) #[node, level]
        level, currEle = 1, []
        while q:
            node, nodeLevel = q.popleft()
            if nodeLevel > level:
                level += 1
                ans.append(currEle)
            currEle = node.val
            if node.left:
                q.append([node.left, nodeLevel+1])
            if node.right:
                q.append([node.right, nodeLevel+1])                
        
        ans.append(currEle)
        return ans