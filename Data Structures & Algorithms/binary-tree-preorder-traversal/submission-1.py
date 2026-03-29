class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        stk = [root]

        while stk:
            curr = stk.pop()
            ans.append(curr.val)
            if curr.right:
                stk.append(curr.right)
            if curr.left:
                stk.append(curr.left)
        
        return ans