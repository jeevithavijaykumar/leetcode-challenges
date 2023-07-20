#102. Binary Tree Level Order Traversal
#Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

import collections

class TreeNode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree():
    def levelordertraversal(self,root):
        res=[]
        q = collections.deque()
        q.append(root)

        while(q):
            level=[]
            for i in range(0,len(q)):
                node = q.popleft()
                if(node):
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if(level):
                res.append(level)
        return(res)


root= TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(11)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
b= BinaryTree()
print(b.levelordertraversal(root))
