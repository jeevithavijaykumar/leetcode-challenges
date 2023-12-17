#112. Path Sum
#Given the root of a binary tree and an integer targetSum,
#return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

class TreeNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BinaryTree():
    def haspathsum(self,root,target):

        def dfs(node,sum):
            if(not node):
                return(False)
            if(not node.left and not node.right):
                return(target== (sum+node.val))
            leftsum = dfs(node.left,sum+node.val)
            rightsum = dfs(node.right, sum+node.val)
            return(leftsum or rightsum)

        return(dfs(root,0))

root= TreeNode(5)
root.left = TreeNode(4)
root.right=TreeNode(8)
root.left.left=TreeNode(11)
root.right.left= TreeNode(13)
root.right.right=TreeNode(4)
b=BinaryTree()
print(b.haspathsum(root,20))