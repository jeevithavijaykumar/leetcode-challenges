#110. Balanced Binary Tree
#Given a binary tree, determine if it is height-balanced

class TreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree():
    def isbalanced(self,root):
        res=[1]
        def balancedBT(root):
            if not root:
                return(0)
            l=balancedBT(root.left)
            r=balancedBT(root.right)
            if(abs(l-r)>1):
                res[0]=0
            return(1+max(l,r))
        if(res[0]==1):
            return(True)
        else:False

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(4)
root.right.left=TreeNode(4)
root.right.right=TreeNode(3)
b=BinaryTree()
print(b.isbalanced(root))