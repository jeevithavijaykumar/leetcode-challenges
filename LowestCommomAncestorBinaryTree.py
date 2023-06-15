#236. Lowest Common Ancestor of a Binary Tree
#Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants
# (where we allow a node to be a descendant of itself).”

class TreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class LowestcommonAncestor():
    def LCABT(self,root,p,q):
        if not root:
            return(None)
        if(p==root.data or q==root.data):
            return(root)
        a=self.LCABT(root.left,p,q)
        b=self.LCABT(root.right,p,q)
        if(a and b):
            return(root)
        if(a or b):
            return(a or b)

root=TreeNode(3)
root.left=TreeNode(5)
root.right=TreeNode(1)
root.left.left=TreeNode(6)
root.left.right=TreeNode(2)
root.left.right.left=TreeNode(7)
root.left.right.right=TreeNode(4)
root.right.left=TreeNode(0)
root.right.right=TreeNode(8)
l=LowestcommonAncestor()
print(l.LCABT(root,5,4))
