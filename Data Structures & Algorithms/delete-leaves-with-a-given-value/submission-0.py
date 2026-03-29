'''
Since we have to delete a given's node's children (if we need to), before evaluating whether the
node itself needs to be deleted (val==target and it is now a leaf node), it makes sense to
implement postorder traversal (left, right, node).
Recursive approach is trivial to implement it. 
'''
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None
        else:
            return root