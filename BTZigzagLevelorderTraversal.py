#103. Binary Tree Zigzag Level Order Traversal
#Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right,
# then right to left for the next level and alternate between).

import collections
class Treenode():
    def __init__(self,val):
        self.left = None
        self.right=None
        self.val = val

class BinaryTree():
    def BTzigzagorder(self,root):
        q= collections.deque()
        q.append(root)
        res=[]
        n=0
        while(q):
            level=[]
            for i in range(0,len(q)):
                node=q.popleft()
                if(node):
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if(level and n%2):
                res.append(level[::-1])
            elif(level):
                res.append(level)
            n=n+1
        return(res)

root = Treenode(3)
root.left = Treenode(9)
root.right = Treenode(20)
root.right.left = Treenode(15)
root.right.right = Treenode(7)
b = BinaryTree()
print(b.BTzigzagorder(root))
