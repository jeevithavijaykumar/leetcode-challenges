#449. Serialize and Deserialize BST
#Design an algorithm to serialize and deserialize a binary search tree.

class TreeNode():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right= None

class BST():
    def serialize(self,root):
        res =[]

        def dfs(node):
            if(not node):
                res.append('N')
                return
            res.append(str(node.data))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return(','.join(res))

    def deserialize(self,data):
        ip = data.split(',')
        self.i=0

        def dfs2():
            if(ip[self.i]=='N'):
                self.i=self.i+1
                return
            node = TreeNode(int(ip[self.i]))
            self.i=self.i+1
            node.left = dfs2()
            node.right = dfs2()
            return node
        return(dfs2())

b = BST()
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(5)
print(b.serialize(root))
print(b.deserialize(b.serialize(root)))




