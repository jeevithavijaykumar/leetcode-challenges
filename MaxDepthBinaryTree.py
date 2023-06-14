#104. Maximum Depth of Binary Tree
#Given the root of a binary tree, return its maximum depth.
#A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class TreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Maxdepth():
    def maxdepthBT(self,root):
        if not root:
            return 0
        else:
            a=self.maxdepthBT(root.left)
            b=self.maxdepthBT(root.right)
            print(a,b)
            return(1+max(a,b))


root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
m=Maxdepth()
print(m.maxdepthBT(root))
