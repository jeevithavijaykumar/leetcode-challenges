#105. Construct Binary Tree from Preorder and Inorder Traversal
#Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree
# and inorder is the inorder traversal of the same tree, construct and return the binary tree.

class TreeNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BinaryTree():
    def BTfromtraversal(self,preorder,inorder):
        if(not preorder or not inorder):
            return(None)
        root=TreeNode(preorder[0])
        mid=inorder.index(preorder[0])
        root.left=self.BTfromtraversal(preorder[1:mid+1],inorder[:mid])
        root.right=self.BTfromtraversal(preorder[mid+1:],inorder[mid+1:])
        return(root)

    def printTree(self,root):
        if(not root):
            return(None)
        self.printTree(root.left)
        print(root.val)
        self.printTree(root.right)
        return

b=BinaryTree()
b.printTree(b.BTfromtraversal([3,9,20,15,7],[9,3,15,20,7]))