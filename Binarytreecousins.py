#993. Cousins in Binary Tree
#Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y,
# return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.
#Two nodes of a binary tree are cousins if they have the same depth with different parents.

class TreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BTcousins():
    def BTcousin(self,root,x,y):
        if (x== root.data or y == root.data):
            return (False)
        def cousins(node,value,height,parent):
            if not node:
                return (0, 0)
            if (value == node.data):
                return (height,parent)
            parent = node.data
            l,px = cousins(node.left, value, height + 1, parent)
            if (l):
                return (l, px)
            r,py = cousins(node.right, value, height + 1, parent)
            if (r):
                return (r, py)
            else:
                return (0,0)
        heightx, parentx = cousins(root, x, 0, -1)
        heighty, parenty = cousins(root, y, 0, -1)
        if (heightx == heighty and parentx != parenty):
            return (True)
        else:
            return(False)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(4)
root.right.left=TreeNode(5)
b=BTcousins()
print(b.BTcousin(root,5,4))