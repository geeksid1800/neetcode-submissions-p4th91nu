'''If the value to be removed has 0 or 1 subtrees, it is a relatively simple task, 
as for a single subtree, it will already be fulfilling the BST property, so you can simply return
the subtree as the node to be removed's child (this effectively cuts out the node to be removed)
    Eg. R       becomes      R, as L is already a proper BST from problem inception
         \                    \
          N                    L
         /
        L
But if N has both L and R subtrees, need to find the correct value in N's subtrees to replace it.
I chose immediately next value of N (call it N'), 
but you can also choose immediately previous value of N in tree.
That way, all other values in the subtree will continue to fulfill BST's property =>
=> values smaller than N  (i.e in N's left subtree) will also be smaller than N'
=>values larger than N (in N's right subtree) will also be larger than N' (as we have chosen smallest
value larger than N as N', and we will be removing N' itself from N's right subtree)
Basically, procedure is find leftmost value in N's right subtree, replace N's val in it's node with
N' value, and then recursively call deleteNode on N.right to remove N' from it
The modified subtree will now be N.right
'''
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
            
            