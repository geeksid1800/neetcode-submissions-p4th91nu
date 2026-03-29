'''
We serialize the Tree into an array using standard preorder traversal. When we encounter a None, append
'N' in it's place. This helps us find leaf nodes and ends of the tree.
While deserializing, we traverse the array using an index. The Ns will help us to decide when we are done
with the left branch while constructing the tree.
First node will always be the current subtree's root. 
If current ix in array is a number, create the node and increment ix, then recursively make fn
calls to node.left = construct() and node.right = construct(). However, if current ix is 'N', then we
have reached a None value (i.e. no more nodes in that branch), so we musn't make any further recursive
calls. That way, when we are done creating the left subtree, the next function call to be executed from
the recursive stack will be to construct node.right. 
'''
class Codec:
    
    def serialize(self, root) -> str:
        self.res = []
        def dfs(node):
            if not node:
                self.res.append("N")
                return
            self.res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return " ".join(self.res)

    def deserialize(self, data):
        self.ix=0
        self.vals = data.split()
        def construct():
            if self.vals[self.ix] == 'N':
                self.ix += 1
                return None
            newNode = TreeNode(int(self.vals[self.ix]))
            self.ix += 1
            newNode.left = construct()
            newNode.right = construct()
            return newNode
        
        root = construct()
        return root