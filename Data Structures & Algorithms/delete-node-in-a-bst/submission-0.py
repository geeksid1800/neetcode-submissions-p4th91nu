# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            '''root.val == key, root is the value to remove
            The first two if statements deal with when root only has 0/1 subtrees
            '''
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            #if root has both subtrees, find the smallest node on it's right (done here) or
            #biggest node on it's left
            nextNode = root.right
            while nextNode.left:
                nextNode = nextNode.left
            #this value will be the immediately larger value than root in the whole tree,
            #you can replace root with this value, and then recursively remove the node
            root.val = nextNode.val
            root.right = self.deleteNode(root.right, root.val)

        return root
            
            