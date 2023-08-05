#116. Populating Next Right Pointers in Each Node
#You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
#Populate each next pointer to point to its next right node.
# If there is no next right node, the next pointer should be set to NULL.

class Treenode():
    def __init__(self,val):
        self.left = None
        self.right=None
        self.val = val
        self.next = None

class BinaryTree():
    def connect(self,root):
        cur=root
        nxt=root.left if root else None

        while(cur and nxt):
            cur.left.next = cur.right
            if(cur.next):
                cur.right.next = cur.next.left
            cur=cur.next
            if(not cur):
                cur=nxt
                nxt=cur.left
        return(root)

root= Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.left = Treenode(4)
root.left.right = Treenode(5)
root.right.left = Treenode(6)
root.right.right = Treenode(7)
b= BinaryTree()
b.connect(root)