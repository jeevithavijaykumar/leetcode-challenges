#226. Invert Binary Tree
#Given the root of a binary tree, invert the tree, and return its root.

class TreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree():
    def InverBT(self,root):
        if not root:
            return 0
        temp=root.left
        root.left=root.right
        root.right=temp

        self.InverBT(root.left)
        self.InverBT(root.right)
        return(root)

root=TreeNode(4)
root.left=TreeNode(2)
root.right=TreeNode(7)
root.left.left=TreeNode(1)
root.left.right=TreeNode(3)
root.right.left=TreeNode(6)
root.right.right=TreeNode(9)
i=BinaryTree()
i.InverBT(root)
