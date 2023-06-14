#700. Search in a Binary Search Tree
#You are given the root of a binary search tree (BST) and an integer val.
#Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
# If such a node does not exist, return null.

class TreeNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BinarySearchTree():
    def searchBST(self,root,val):
        curr=root
        while(curr):
            if(curr.val==val):
                return(curr)
            if(curr.val>val):
                curr=curr.left
            if(curr.val<val):
                curr=curr.right
        return(None)

root=TreeNode(4)
root.left=TreeNode(2)
root.right=TreeNode(7)
root.left.left=TreeNode(1)
root.left.right=TreeNode(3)
b=BinarySearchTree()
print(b.searchBST(root,3))
