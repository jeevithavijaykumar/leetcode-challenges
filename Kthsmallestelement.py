#230. Kth Smallest Element in a BST
#Given the root of a binary search tree, and an integer k,
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

class TreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BSTKth():
    def kthsmallelement(self,root,k):
        res=[]

        def inordertrav(root):
            if(root.left):
                inordertrav(root.left)
            if(root):
                res.append(root.data)
            if(root.right):
                inordertrav(root.right)
        inordertrav(root)
        return (res[k - 1])

root=TreeNode(3)
root.left=TreeNode(1)
root.right=TreeNode(4)
root.left.right=TreeNode(2)
b=BSTKth()
print(b.kthsmallelement(root,2))

