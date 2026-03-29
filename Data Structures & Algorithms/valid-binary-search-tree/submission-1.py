
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        Doing in-order traversal should yield a strictly increasing seq.
        Instead of storing the answer of inorder traversal, simply store the previous element.
        Here I am implementing the iterative version of in-order traversal
        '''
        prev = -1001
        stk = []
        curr = root
        while curr or stk:
            if curr:
                stk.append(curr)
                curr = curr.left
            else:
                midNode = stk.pop()
                if prev >= midNode.val:
                    return False
                prev = midNode.val
                curr = midNode.right
        
        return True
