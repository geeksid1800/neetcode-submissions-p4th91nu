class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)
        if not root:
            return newNode

        curr = root
        while True:
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = newNode
                    break
            
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = newNode
                    break
            
        
        return root