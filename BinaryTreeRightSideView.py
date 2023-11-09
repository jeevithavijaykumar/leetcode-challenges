#199. Binary Tree Right Side View
#Given the root of a binary tree, imagine yourself standing on the right side of it
#Return the values of the nodes you can see ordered from top to bottom.

class Treenode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BinaryTree():
    def rightsideview(self,root):
        q=[root]
        res=[]

        while(q):
            rightside=None
            for i in range(0,len(q)):
                node=q.pop(0)
                if node:
                    rightside=node
                    q.append(node.left)
                    q.append(node.right)
            if(rightside):
                res.append(rightside.val)

        return(res)

root=Treenode(1)
root.left=Treenode(2)
root.right=Treenode(3)
root.left.right=Treenode(5)
root.right.right=Treenode(4)
b=BinaryTree()
print(b.rightsideview(root))