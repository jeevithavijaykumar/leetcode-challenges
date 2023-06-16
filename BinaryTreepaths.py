#257. Binary Tree Paths
#Given the root of a binary tree, return all root-to-leaf paths in any order.
#A leaf is a node with no children.

class TreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTreepath():
    def BTpath(self,root):
        res=[]
        def Btpaths(node,path,res):
            if not node:
                return(res)
            if not node.left and not node.right:
                res.append(path)
                return(res)
            if node.left:
                Btpaths(node.left,path+f"->{node.left.data}",res)
            if node.right:
                Btpaths(node.right,path+f"->{node.right.data}",res)
            return(res)
        return(Btpaths(root,f"{root.data}",res))

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(5)
b=BinaryTreepath()
print(b.BTpath(root))
