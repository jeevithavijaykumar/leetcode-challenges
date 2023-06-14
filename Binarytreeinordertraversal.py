#94. Binary Tree Inorder Traversal
#Given the root of a binary tree, return the inorder traversal of its nodes' values.

class TreeNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BTInorder():
    def inordertraversal(self,root):
        res=[]
        def inorder(root):
            if(not root):
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return(res)

root=TreeNode(1)
root.left=TreeNode(None)
root.right=TreeNode(2)
root.right.left=TreeNode(3)
b=BTInorder()
print(b.inordertraversal(root))
