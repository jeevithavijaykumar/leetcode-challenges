#111. Minimum Depth of Binary Tree
#Given a binary tree, find its minimum depth.
#The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

class TreeNode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right=None

class BinaryTree():
    def minimumdepth(self,root):
        if(not root):
            return 0
        else:
            a = self.minimumdepth(root.left)
            b=self.minimumdepth(root.right)
            if(not root.left and not root.right):
                return(1)
            if(not root.left):
                return(1+b)
            if(not root.right):
                return(1+a)
            return(1+min(a,b))

root = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
root.right.right.right.right = TreeNode(6)
b= BinaryTree()
print(b.minimumdepth(root))