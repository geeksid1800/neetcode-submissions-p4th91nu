'''
Recursive approach is obvious. Here is the iterative approach:
maintain a stack, when you encounter a node, add it to result, and then node.right and then node.left
This is because then node.left will be popped first and the left subtree will be added to stk and
also result first, followed by right subtree.
'''
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