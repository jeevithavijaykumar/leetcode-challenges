#235. Lowest Common Ancestor of a Binary Search Tree
#Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
#“The lowest common ancestor is defined between two nodes p and q as the lowest node in T
# that has both p and q as descendants (where we allow a node to be a descendant of itself).

class TreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST():
    def LCA(self,p,q):
        curr=root
        while(curr):
            if(curr.val>p.val and curr.val>q.val):
                curr=curr.left
            if (curr.val < p.val and curr.val < q.val):
                curr = curr.right
            else:
                return(curr)
root=TreeNode(6)



