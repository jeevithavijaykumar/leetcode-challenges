#129. Sum Root to Leaf Numbers
#You are given the root of a binary tree containing digits from 0 to 9 only.
#Each root-to-leaf path in the tree represents a number.
#Return the total sum of all root-to-leaf numbers.

class TreeNode():
    def __init__(self,val):
        self.val =val
        self.left=None
        self.right =None

class BinaryTree():
    def sumroottoleaf(self,root):

        def dfs (node,num):
            if(not node):
                return(0)
            num=num*10+node.val
            if(not node.left and not node.right):
                return(num)
            return(dfs(node.left,num) + dfs(node.right,num))

        return(dfs(root,0))

t=TreeNode(4)
t.left = TreeNode(9)
t.right = TreeNode(0)
t.left.left = TreeNode(5)
t.left.right = TreeNode(1)
b= BinaryTree()
print(b.sumroottoleaf(t))



