#222. Count Complete Tree Nodes.
# Given the root of a complete binary tree, return the number of the nodes in the tree.

class TreeNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BinaryTree():
    def countNodes(self,root):

        def dfs(node):
            if(not node):
                return(0)
            return(dfs(node.left)+dfs(node.right)+1)

        return(dfs(root))

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(4)
b=BinaryTree()
print(b.countNodes(root))

