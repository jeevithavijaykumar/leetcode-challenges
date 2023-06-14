#100. Same Tree
#Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class TreeNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class SameTree():
    def issame(self,p,q):
        if(not p and not q):
            return(True)
        if((not p and q) or (p and not q)):
            return(False)
        if(p.val != q.val):
            return(False)
        a=self.issame(p.left,q.left)
        b = self.issame(p.right,q.right)
        return(a and b)

p=TreeNode(1)
p.left=TreeNode(2)
p.right=TreeNode(3)
q=TreeNode(1)
q.left=TreeNode(2)
q.right=TreeNode(3)
s=SameTree()
print(s.issame(p,q))
