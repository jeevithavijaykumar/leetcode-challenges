#543. Diameter of Binary Tree
#Given the root of a binary tree, return the length of the diameter of the tree.
#The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.

class Treenode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Binarytree():
    def diameterBT(self,root):
        self.maxdia=0

        def maxdiameter(root):
            if(not root):
                return(0)
            a=maxdiameter(root.left)
            b=maxdiameter(root.right)
            self.maxdia=max(self.maxdia,a+b)
            return(1+max(a,b))
        maxdiameter(root)
        return(self.maxdia)

root=Treenode(1)
root.left=Treenode(2)
root.right=Treenode(3)
root.left.left=Treenode(4)
root.left.right=Treenode(5)
b=Binarytree()
print(b.diameterBT(root))
