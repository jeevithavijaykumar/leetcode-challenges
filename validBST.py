#98. Validate Binary Search Tree
#Given the root of a binary tree, determine if it is a valid binary search tree (BST)
#A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
#The right subtree of a node contains only nodes with keys greater than the node's key.
#Both the left and right subtrees must also be binary search trees.

class TreeNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class ValidBinarySeachTree():
    def isvalidtree(self,root):
        def validbst(root,left,right):
            if(not root):
                return(True)
            if(not(root.val>left and root.val<right)):
                return(False)
            a=validbst(root.left,left,root.val)
            b=validbst(root.right,root.val,right)
            return(a and b)
        c=validbst(root,float('-inf'),float('inf'))
        return(c)

v=TreeNode(2)
v.left=TreeNode(1)
v.right=TreeNode(3)
i=ValidBinarySeachTree()
print(i.isvalidtree(v))

root=TreeNode(5)
root.left=TreeNode(1)
root.right=TreeNode(4)
root.right.left=TreeNode(3)
root.right.right=TreeNode(6)
v=ValidBinarySeachTree()
print(v.isvalidtree(root))









class TreeNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


class ValisBST():
    def valid(self,root):

        def isvalid(node,left,right):

            if(not node):
                return(True)
            print(node.val)
            print(left)
            print(right)
            if(not ((node.val>left and (node.val<right)))):
                return(False)
            return(isvalid(node.left,left,node.val) and isvalid(node.right,node.val,right))
        output=isvalid(root,float('-inf'),float('inf'))
        return(output)

root=TreeNode(5)
root.left=TreeNode(1)
root.right=TreeNode(7)
root.right.left=TreeNode(6)
root.right.right=TreeNode(8)
v=ValisBST()
print(v.valid(root))



