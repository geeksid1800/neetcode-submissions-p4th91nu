'''
Inorder traversal + take kth element
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk = []
        cnt = 0
        curr = root
        while stk or curr:
            if curr:
                stk.append(curr)
                curr = curr.left
            else:
                #the last node added to stack had no left children
                midNode = stk.pop()
                cnt += 1
                if cnt == k:
                    return midNode.val
                curr = midNode.right