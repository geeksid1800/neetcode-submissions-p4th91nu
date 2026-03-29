'''
Iterative solution of postorder traversal:
Given a Tree N, the postorder traversal will be [L,R,N]. Reversing it gives us [N,R,L]
            / \
           L   R
[N,R,L] can be achieved very similarly to preorder traversal([N,L,R]).
'''
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        stk =[root]

        while stk:
            node = stk.pop()
            ans.append(node.val)
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)
        
        ans.reverse()
        return ans
        